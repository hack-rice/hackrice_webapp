from hackrice import db


class Reviewer(db.Model):
	"""
	Hackrice Reviewer database model.
	"""
    id = db.Column(db.Integer, primary_key=True, autoincrement = True)
    email = db.Column(db.String(80), unique = True)
    name = db.Column(db.String(60), index = True)

    def __repr__(self):
        return '<Reviewer %r>' % (self.name)
