import datetime
from flask_sqlalchemy import SQLAlchemy
from hackrice import db


class Applicant(db.model):
    """
    Represents an applicant to HackRice. Initially, status is set to 0 for a non-reviewed application.
    Afterwards, status will be either (1) for accepted (2) for hold or (3) for rejected.
    The store will be used to automatically set the status, and initially the score is set to -1, which
    represents an unscored/unreviewed application.
    """
    id = db.Column(db.INTEGER, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    email = db.Column(db.String, unique=True)
    date = db.Column(db.Date)
    org = db.Column(db.String(100))
    resume = db.Column(db.LargeBinary)
    git_hub = db.Column(db.String(200))
    linked_in = db.Column(db.String(200))
    score = db.Column(db.INTEGER, default=-1)
    status = db.Column(db.INTEGER)
    created_at = db.Column(db.INTEGER, default=datetime.datetime.now)
