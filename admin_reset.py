import sys
from app import app  # Import your Flask app instance
from models.team import Team, db

def reset_team(team_name):
    with app.app_context():
        # Search for the team by name
        team = Team.query.filter_by(team_name=team_name).first()
        
        if not team:
            print(f"❌ Error: Team '{team_name}' not found.")
            return

        # Reset violations and status
        team.violations = 0
        db.session.commit()
        
        print(f"✅ Success: Team '{team_name}' has been reinstated.")
        print(f"📊 Current Stats -> Score: {team.total_score}, Violations: {team.violations}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python admin_reset.py <team_name>")
    else:
        target_team = sys.argv[1]
        reset_team(target_team)