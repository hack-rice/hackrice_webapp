from flask_wtf import Form
from wtforms import StringField, BooleanField, SelectField, DateField
from wtforms.validators import DataRequired


class ApplyForm(Form):
	email = StringField('applicant_email', validators = [DataRequired()], render_kw={"placeholder": "email"})
	password = StringField('applicant_password', validators = [DataRequired()], render_kw={"placeholder": "password"}, )
	first_name = StringField('applicant_first_name', validators = [DataRequired()], render_kw={"placeholder": "First Name"})
	last_name = StringField('applicant_last_name', validators = [DataRequired()], render_kw={"placeholder": "Last Name"})
	date = DateField('applicant_date', validators = [DataRequired()])
	university = SelectField('applicant_univ', validators = [DataRequired()])
	github = StringField('applicant_github', render_kw={"placeholder": "Github"})
	linkedin = StringField('applicant_linkedin', render_kw={"placeholder": "Linkedin"})
	website = StringField('applicant_website', render_kw={"placeholder": "mywebsite.com"}) 

	

