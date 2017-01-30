"""
Methods related to managing user data. Primarily for testing the templating methods.
"""


class User:
    """
    Class for managing user data when passing between the different parts of the application.
    """

    def __init__(self, id, name, app_quota, apps_overdue, due_date):
        self.id = id
        self.name = name
        self.app_quota = app_quota
        self.apps_overdue = apps_overdue
        self.due_date = due_date


def make_fake_users():
    """
    Function to make some fake users for testing the users in the user review template.
    :return: users - a list of user objects
    """
    names = ['bob', 'alice', 'joe', 'thomas', 'james']
    users = []
    for i in range(5):
        users.append(User(i, names[i], i, i, i))

    return users
