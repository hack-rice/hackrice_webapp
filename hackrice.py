from __future__ import with_statement
from contextlib import closing
from flask import Flask, render_template, g
import sqlite3

app = Flask(__name__)
app.config.from_envvar('FLASKR_SETTINGS', silent=True)

def init_db():
    with closing(connect_db()) as db:
        with app.open_resource('schema.sql') as f:
            db.cursor().executescript(f.read())
        db.commit()


def connect_db():
    return sqlite3.connect('/tmp/hackrice.db')

@app.cli.command('initdb')
def initdb_command():
    """Creates the database tables."""
    init_db()
    print('Initialized the database.')

def get_db():
    """Opens a new database connection if there is none yet for the
    current application context.
    """
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db


@app.teardown_appcontext
def close_db(error):
    """Closes the database again at the end of the request."""
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()

def insert(table, fields=(), values=()):
    # g.db is the database connection
    cur = get_db().cursor()
    query = 'INSERT INTO %s (%s) VALUES (%s)' % (
        table,
        ', '.join(fields),
        ', '.join(['?'] * len(values))
    )
    cur.execute(query, values)
    get_db().commit()
    id = cur.lastrowid
    cur.close()
    return id

def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv

"""
@app.route('/')
def show_entries():
    db = get_db()
    cur = db.execute('select title, text from entries order by id desc')
    entries = cur.fetchall()
    return render_template('show_entries.html', entries=entries)
"""


@app.route('/')
def index():
    """
    Loads the index page.
    """
    #insert('responses', ('user_id', 'email', 'first_name', 'last_name'), ('a', 'a', 'a', 'a'))
    user = query_db('select * from responses', one=True)
    print user
    return render_template('index.html')


@app.route('/scoring')
def scoring():
    """
    Loads the index page.
    """
    return render_template('scoring.html')
