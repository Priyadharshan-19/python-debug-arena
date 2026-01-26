import time
from flask import Blueprint, request, jsonify, session
from services.code_runner import execute_python_code
from levels.level_manager import LEVELS
from models.team import db, Team
from models.submission import Submission

submit_bp = Blueprint('submit', __name__)

@submit_bp.route('/run_code/<int:level_id>', methods=['POST'])
def run_code(level_id):
    data = request.json
    user_code = data.get('code')

    # 🔒 Safety checks
    if not user_code:
        return jsonify({
            "success": False,
            "message": "No code provided."
        })

    if 'team_id' not in session:
        return jsonify({
            "success": False,
            "message": "Unauthorized access."
        })

    # 1️⃣ Execute the user code safely
    result = execute_python_code(user_code)

    # 2️⃣ Load level data
    level = LEVELS.get(level_id)
    if not level:
        return jsonify({
            "success": False,
            "message": "Invalid level."
        })

    expected = level['expected_output']

    # 3️⃣ SUCCESS CASE
    if result['status'] == 'success' and result['output'] == expected:

        # ⏱️ TIME CALCULATION
        start_time = session.get('level_start_time', time.time())
        end_time = time.time()
        time_taken = int(end_time - start_time)

        # 🧮 BASE SCORING
        base_points = 100
        time_penalty = time_taken // 10   # -1 point per 10 seconds
        level_score = max(50, base_points - time_penalty)

        # 💡 HINT PENALTY LOGIC
        hint_key = f"hint_used_level_{level_id}"
        if session.get(hint_key):
            penalty = level.get('penalty', 10)
            level_score -= penalty
            level_score = max(30, level_score)  # hard minimum score

        # 🏆 UPDATE TEAM PROGRESS
        team = Team.query.get(session['team_id'])

        if team.current_level == level_id:
            team.current_level += 1
            team.total_score += level_score

            # 📝 SAVE SUBMISSION RECORD
            submission = Submission(
                team_id=team.id,
                level_id=level_id,
                code_submitted=user_code,
                status='Correct',
                time_taken=time_taken,
                score_earned=level_score
            )

            db.session.add(submission)
            db.session.commit()

            # 🧹 CLEAN SESSION STATE
            session.pop('level_start_time', None)
            session.pop('current_level_id', None)
            session.pop(hint_key, None)

        return jsonify({
            "success": True,
            "message": "Correct! Next level unlocked 🎉",
            "time_taken": time_taken,
            "score_earned": level_score,
            "total_score": team.total_score
        })

    # ❌ FAILURE CASE
    actual_output = (
        result['output']
        if result['status'] == 'success'
        else f"Error: {result['output']}"
    )

    return jsonify({
        "success": False,
        "message": "Output mismatch or execution error.",
        "output": actual_output
    })
