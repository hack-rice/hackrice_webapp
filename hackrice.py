from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from forms import ApplyForm
# from .forms import ApplyForm

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
from users import make_fake_users, User


@app.route('/')
def index():
    """
    Loads the index page.
    """
    form = ApplyForm()
    return render_template('index.html', form = form)


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

@app.route('/review-application/<uid>')
def review_application(uid):
    """
    Loads the interface for reviewing an application 
    corresponding to user with id `uid`.
    """
    return render_template('review.html', uid=uid)