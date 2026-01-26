import time
from flask import Blueprint, render_template, session, redirect, url_for, abort, jsonify, request
from models.team import Team, db  # Ensure db is imported correctly from your models
from levels.level_manager import LEVELS

arena = Blueprint('arena', __name__)

# =======================
# DASHBOARD (DYNAMIC + GATEKEEPER)
# =======================
@arena.route('/dashboard')
def dashboard():
    if 'team_id' not in session:
        return redirect(url_for('auth.login'))

    team = Team.query.get(session['team_id'])

    # 🚫 GATEKEEPER: Block disqualified teams
    if team.violations >= 3:
        return redirect(url_for('arena.disqualified'))

    # Dynamically build levels list from LEVELS manager
    levels_list = []
    for level_id, data in LEVELS.items():
        levels_list.append({
            'id': level_id,
            'name': data['title'],
            'difficulty': data['difficulty']
        })

    # Ensure correct order: Level 1 through Level 8
    levels_list.sort(key=lambda x: x['id'])

    return render_template(
        'dashboard.html',
        team=team,
        levels=levels_list
    )


# =======================
# ARENA (LEVEL PAGE)
# =======================
@arena.route('/arena/<int:level_id>')
def level_detail(level_id):
    if 'team_id' not in session:
        return redirect(url_for('auth.login'))

    team = Team.query.get(session['team_id'])

    # 🚫 Extra safety: block disqualified teams from entering any level
    if team.violations >= 3:
        return redirect(url_for('arena.disqualified'))

    total_levels = max(LEVELS.keys())

    # 🏆 Check if they already finished all levels
    if team.current_level > total_levels:
        return redirect(url_for('arena.victory'))

    # 🔐 Prevent skipping ahead
    if level_id > team.current_level:
        return redirect(url_for('arena.dashboard'))

    level = LEVELS.get(level_id)
    if not level:
        abort(404)

    # ⏱️ Level Timer Logic
    if session.get('current_level_id') != level_id:
        session['current_level_id'] = level_id
        session['level_start_time'] = time.time()

    return render_template(
        'arena.html',
        level=level,
        level_id=level_id,
        team=team,
        total_levels=total_levels
    )


# =======================
# HINT API (WITH PENALTY)
# =======================
@arena.route('/get_hint/<int:level_id>', methods=['POST'])
def get_hint(level_id):
    if 'team_id' not in session:
        return jsonify({"success": False, "message": "Unauthorized"}), 401

    level = LEVELS.get(level_id)
    if not level:
        return jsonify({"success": False, "message": "Invalid level"}), 404

    # Record that a hint was used to apply score penalties later
    session[f"hint_used_level_{level_id}"] = True

    return jsonify({
        "success": True,
        "hint": level["hint"],
        "penalty": level.get("penalty", 0)
    })


# =======================
# 🚨 VIOLATION LOGGER (DB PERSISTENT)
# =======================
@arena.route('/log_violation', methods=['POST'])
def log_violation():
    if 'team_id' not in session:
        return jsonify({"success": False}), 401

    team = Team.query.get(session['team_id'])
    
    # Optional: Log the reason sent from proctor.js (tab_switch or exit_fullscreen)
    data = request.get_json()
    reason = data.get('reason', 'unknown_policy_violation')

    # Increment and save to DB
    team.violations += 1
    db.session.commit()

    return jsonify({
        "success": True,
        "violations": team.violations,
        "disqualified": team.violations >= 3,
        "reason_logged": reason
    })


# =======================
# 🚫 DISQUALIFIED PAGE
# =======================
@arena.route('/disqualified')
def disqualified():
    if 'team_id' not in session:
        return redirect(url_for('auth.login'))

    team = Team.query.get(session['team_id'])

    # If they haven't actually hit the limit, don't let them see this page
    if team.violations < 3:
        return redirect(url_for('arena.dashboard'))

    return render_template('disqualified.html', team=team)


# =======================
# 🏆 VICTORY PAGE
# =======================
@arena.route('/victory')
def victory():
    if 'team_id' not in session:
        return redirect(url_for('auth.login'))

    team = Team.query.get(session['team_id'])
    total_levels = max(LEVELS.keys())

    # Redirect back if they haven't actually finished Level 8
    if team.current_level <= total_levels:
        return redirect(url_for('arena.dashboard'))

    return render_template('victory.html', team=team)