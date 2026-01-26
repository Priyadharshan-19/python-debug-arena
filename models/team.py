from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Team(db.Model):
    __tablename__ = 'team'  # Explicit table name

    id = db.Column(db.Integer, primary_key=True)
    team_name = db.Column(db.String(50), unique=True, nullable=False)
    college = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)

    current_level = db.Column(db.Integer, default=1)
    total_score = db.Column(db.Integer, default=0)

    # ✅ NEW FIELD
    violations = db.Column(db.Integer, default=0)

    # Relationships
    submissions = db.relationship(
        'Submission',
        back_populates='team',
        lazy=True
    )
