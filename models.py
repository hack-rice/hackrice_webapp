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
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    email = db.Column(db.String, unique=True)
    date = db.Column(db.Date)
    org = db.Column(db.String(100))
    resume = db.Column(db.LargeBinary)
    git_hub = db.Column(db.String(200))
    linked_in = db.Column(db.String(200))
    score = db.Column(db.Integer, default=-1)
    status = db.Column(db.Integer)
    created_at = db.Column(db.Integer, default=datetime.datetime.now)

class Reviewer(db.Model):
	"""
	Hackrice Reviewer database model.
	"""
    id = db.Column(db.Integer, primary_key=True, autoincrement = True)
    email = db.Column(db.String(80), unique = True)
    name = db.Column(db.String(60), index = True)

    def __repr__(self):
        return '<Reviewer %r>' % (self.name)

class Review_Form(db.Model):
    """
    Database model for reviewing applications
    """
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    applicant_email = db.Column(db.String(80), unique = True)
    applicant_name = db.Column(db.String(60), index =True)
    projects_exist = db.Column(db.Boolean, server_default = False)
    projects_sig = db.Column(db.Boolean, server_default = False)
    website_exist = db.Column(db.Boolean, server_default = False)
    internship = db.Column(db.Boolean, server_default = False)
    cs_award = db.Column(db.Boolean, server_default = False)
    research_or_startup = db.Column(db.Boolean, server_default = False)
    answered_frq = db.Column(db.Boolean, server_default = False)
    good_frq_answer = db.Column(db.Boolean, server_default = False)
    score = db.Column(db.Integer, inex = True)
