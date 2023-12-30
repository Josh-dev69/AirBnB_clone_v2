#!/usr/bin/python3
"""
Start a Flask web application that display "Hello HBNB!"
"""
from flask import Flask

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    Function to display 'Hello HBNB!' on the root route.
    """
    return 'Hello HBNB!'

if __name__ == '__main__':
    app.run()
