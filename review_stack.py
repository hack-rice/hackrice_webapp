"""
Implements the methods for querying the SQL database
to get the next applicant to review and to update the
database with a reviewed applicant
"""

def get_next_applicant(Applicants):
    """
    Given a database of Applicant models
    returns the Applicant that needs to be reviewed next
    """
    return Applicants.query.order_by(Applicants.created_at).filter_by(score=-1).first()
