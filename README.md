Fitness and Nutrition Logger

A full-stack web application built with Python, Flask, and SQLAlchemy for tracking workouts and (in progress) nutrition. Originally based on a college senior project, rebuilt from scratch with expanded functionality and a stronger focus on secure, well-structured backend design.

Features (current)

User accounts with secure signup/login, using hashed passwords (Werkzeug) and session-based authentication
Protected routes — pages and actions are only accessible to logged-in users
Full exercise logging (create, read, update, delete):
Strength entries: exercise name, date, sets, reps, weight (lbs)
Cardio entries: exercise name, date, duration (min), distance (mi), calories burned
Per-user data isolation — users can only view, edit, or delete their own logged exercises
Dynamic, JavaScript-driven form that adjusts input fields based on exercise type

Planned

Nutrition tracking: set a daily caloric target, log food eaten, and track calories against that target

Built with: Python, Flask, SQLAlchemy, SQLite, HTML/CSS, JavaScript