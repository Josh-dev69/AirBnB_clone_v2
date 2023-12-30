#!/usr/bin/python3
"""
Start a Flask web application.

"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    Function to display 'Hello HBNB!'.
    """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    Function to display 'HBNB'.
    """
    return 'HBNB'


if __name__ == '__main__':
    app.run()
