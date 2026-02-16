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

# Database URI
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv(
    'DATABASE_URL',
    'sqlite:///' + os.path.join(basedir, 'instance', 'db.sqlite3')
)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Ensure instance folder exists
try:
    os.makedirs(os.path.join(basedir, 'instance'), exist_ok=True)
except OSError:
    pass

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
# CREATE TABLES
# =========================
with app.app_context():
    db.create_all()

# =========================
# ROUTES
# =========================
@app.route('/')
def index():
    return render_template('index.html')

# ✅ Loader.io verification route
@app.route('/loaderio-8b703d115e5e1a915c05b0408c49b1a6.txt')
def loaderio_verification():
    return "loaderio-8b703d115e5e1a915c05b0408c49b1a6"

# =========================
# ENTRY POINT
# =========================
if __name__ == '__main__':
    app.run(debug=True)
