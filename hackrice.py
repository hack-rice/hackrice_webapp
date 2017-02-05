from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)
from users import make_fake_users, User


@app.route('/')
def index():
    """
    Loads the index page.
    """
    return render_template('index.html')


@app.route('/scoring')
def scoring():
    """
    Loads the index page.
    """
    return render_template('scoring.html')


@app.route('/review-admin')
def review_admin():
    """
    Loads the admin interface for managing HackRice reviewers.
    """
    user_list = make_fake_users()
    # selected = User(1, "Bob", 1, 1, 1)
    return render_template('review-admin.html', users=user_list)

