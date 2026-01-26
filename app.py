import os
from flask import Flask, render_template
from models.team import db, Team
from models.submission import Submission
from routes.auth_routes import auth
from routes.arena_routes import arena
from routes.submit_routes import submit_bp
from routes.leaderboard_routes import leaderboard_bp

# Base directory
basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

# =========================
# CONFIGURATION
# =========================

# Secret Key (env first, fallback for local)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev-key-123')

# Database URI (env first, fallback to SQLite)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv(
    'DATABASE_URL',
    'sqlite:///' + os.path.join(basedir, 'database', 'db.sqlite3')
)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# =========================
# INITIALIZE EXTENSIONS
# =========================
db.init_app(app)

# =========================
# REGISTER BLUEPRINTS
# =========================
app.register_blueprint(auth)
app.register_blueprint(arena)
app.register_blueprint(submit_bp)
app.register_blueprint(leaderboard_bp)

# =========================
# CREATE TABLES (SAFE)
# =========================
with app.app_context():
    db.create_all()

# =========================
# ROUTES
# =========================
@app.route('/')
def index():
    return render_template('index.html')

# =========================
# ENTRY POINT
# =========================
if __name__ == '__main__':
    app.run(debug=True)
