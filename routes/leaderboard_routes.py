from flask import Blueprint, render_template
from models.team import Team

leaderboard_bp = Blueprint('leaderboard', __name__)

@leaderboard_bp.route('/leaderboard')
def show_leaderboard():
    # Sort by current_level (descending) and then total_score (descending)
    teams = Team.query.order_by(Team.current_level.desc(), Team.total_score.desc()).all()
    
    return render_template('leaderboard.html', teams=teams)