#!/usr/bin/python3
"""
Start a Flask web application.

"""

from flask import Flask, url_for

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    function to display Hello HBNB!.
    """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    function to HBNB
    """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """ routing to c with parameters"""
    if '_' in text:
        text = text.replace('_', ' ')
    return f"C {text}"


if __name__ == "__main__":
    app.run()
