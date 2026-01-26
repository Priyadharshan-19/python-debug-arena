from datetime import datetime
from models.team import db

class Submission(db.Model):
    __tablename__ = 'submission'
    id = db.Column(db.Integer, primary_key=True)
    team_id = db.Column(db.Integer, db.ForeignKey('team.id'), nullable=False)
    level_id = db.Column(db.Integer, nullable=False)
    code_submitted = db.Column(db.Text, nullable=False)
    status = db.Column(db.String(20), nullable=False)
    time_taken = db.Column(db.Integer)
    score_earned = db.Column(db.Integer)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    # Add this to link back to Team
    team = db.relationship('Team', back_populates='submissions')