import sys
import os

# Add project root to sys.path
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(PROJECT_ROOT)

from app import app
from models.team import db, Team
from models.submission import Submission

# Ensure database directory exists
DB_DIR = os.path.join(PROJECT_ROOT, "database")
os.makedirs(DB_DIR, exist_ok=True)

with app.app_context():
    db.create_all()
    print("✅ Database initialized successfully at database/db.sqlite3")
