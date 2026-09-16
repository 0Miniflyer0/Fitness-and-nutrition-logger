from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'some-secret-key'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = User.query.filter_by(username=username).first()

        if user is None:
            flash("Username does not exist.")
            return redirect(url_for('login'))

        if not check_password_hash(user.password_hash, password):
            flash("Incorrect password.")
            return redirect(url_for('login'))

        session['user_id'] = user.id
        return redirect(url_for('dashboard'))
    return render_template('login.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        confirm_password = request.form['confirm_password']

        if password != confirm_password:
            flash("Passwords do not match!")
            return redirect(url_for('signup'))

        new_user = User(username=username, password_hash=generate_password_hash(password))
        db.session.add(new_user)
        db.session.commit()
        return render_template('signup_success.html')
    return render_template('signup.html')

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    return render_template('dashboard.html')

@app.route('/log-exercise', methods=['GET', 'POST'])
def log_exercise():
    if request.method == 'POST':
        date = request.form['date']
        exercise_name = request.form['exercise_name']
        exercise_type = request.form['type']

        if exercise_type =='strength':
            date = request.form['date']
            sets = request.form['sets']
            reps = request.form['reps']
            weight = request.form['weight']
            duration = None
            distance = None
            calories = None
        elif exercise_type == 'cardio':
            date = request.form['date']
            sets = None
            reps = None
            weight = None
            duration = request.form['duration']
            distance = request.form['distance']
            calories = request.form['calories']

        new_log=ExerciseLog(
            user_id=session['user_id'],
            date=date,
            type=exercise_type,
            exercise_name=exercise_name,
            sets=sets,
            reps=reps,
            weight=weight,
            duration=duration,
            distance=distance,
            calories=calories
        )
        db.session.add(new_log)
        db.session.commit()
    return render_template('log_exercise.html')

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(200), nullable=False)

class ExerciseLog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    date = db.Column(db.Date, nullable=False)
    type = db.Column(db.String(20), nullable=False)
    exercise_name = db.Column(db.String(100), nullable=False)
    sets = db.Column(db.Integer, nullable=True)
    reps = db.Column(db.Integer, nullable=True)
    weight = db.Column(db.Float, nullable=True)
    duration = db.Column(db.Float, nullable=True)
    distance = db.Column(db.Float, nullable=True)
    calories = db.Column(db.Integer, nullable=True)


if __name__ == '__main__':
    app.run(debug=True)