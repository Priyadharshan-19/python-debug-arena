from flask import Blueprint, render_template, redirect, url_for, request, flash, session
from werkzeug.security import generate_password_hash, check_password_hash
from models.team import db, Team

auth = Blueprint('auth', __name__)

@auth.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        team_name = request.form.get('team_name')
        email = request.form.get('email')
        college = request.form.get('college')
        password = request.form.get('password')

        # Check if team already exists
        user = Team.query.filter_by(team_name=team_name).first()
        if user:
            flash('Team name already exists!', 'error')
            return redirect(url_for('auth.register'))

        # Create new team with hashed password
        new_team = Team(
            team_name=team_name,
            email=email,
            college=college,
            password=generate_password_hash(password, method='pbkdf2:sha256')
        )

        db.session.add(new_team)
        db.session.commit()
        flash('Registration successful! Please login.', 'success')
        return redirect(url_for('auth.login'))

    return render_template('register.html')

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        team_name = request.form.get('team_name')
        password = request.form.get('password')
        
        team = Team.query.filter_by(team_name=team_name).first()
        
        if team and check_password_hash(team.password, password):
            session['team_id'] = team.id
            session['team_name'] = team.team_name
            return redirect(url_for('index')) # Redirect to dashboard later
        else:
            flash('Invalid credentials!', 'error')
            
    return render_template('login.html')

@auth.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))