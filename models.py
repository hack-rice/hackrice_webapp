import datetime

from hackrice import db


class Applicant(db.Model):
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

    def __init__(self, first_name, last_name, email, date, org, resume, git_hub, linked_in, score, status):
        """
        Initializes Applicant Object
        """
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.date = date
        self.org = org
        self.resume = resume
        self.git_hub = git_hub
        self.linked_in = linked_in
        self.score = score
        self.status = status


class Reviewer(db.Model):
    """
    Hackrice Reviewer database model.
    """
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(80), unique=True)
    name = db.Column(db.String(60), index=True)


    def __init__(self,email,name):
        """
        Initializes Reviewer Object
        """
        self.email = email
        self.name = name

    def __repr__(self):
        return '<Reviewer %r>' % (self.name)


class Acceptance(db.Model):
    """
    Hack Rice Database schema for Acceptance responses from accepted applicants. Should have a relationship with
    applicant model id.
    """

    id = db.Column(db.INTEGER, primary_key=True, autoincrement=True)
    attending = db.Column(db.BOOLEAN)
    shirt = db.Column(db.String(10))
    sleep_arange = db.Column(db.String(10))
    traveling = db.Column(db.String(80))
    travel_cost = db.Column(db.INTEGER)
    diet = db.Column(db.String(200))

    # Potentially make acceptance id the primary key?
    applicant_id = db.Column(db.Integer, db.ForeignKey('applicant.id'))
    applicant = db.relationship('Applicant',
                                backref=db.backref('acceptance', lazy='dynamic'))

    def __init__(self,attending,shirt,sleep_arrange,traveling,travel_cost,diet):
        """
        Initializes Acceptance Object
        """
        self.attending = attending
        self.shirt = shirt
        self.sleep_arange = sleep_arrange
        self.traveling = traveling
        self.travel_cost = travel_cost
        self.diet = diet