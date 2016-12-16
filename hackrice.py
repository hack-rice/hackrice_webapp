from flask import Flask, render_template
app = Flask(__name__)

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
