#!/usr/bin/python3
"""
Start a Flask web application.

Web application listens on 0.0.0.0, port 5000.
Routes:
    /: display "Hello HBNB!"
Use the option strict_slashes=False in route definition.
"""
from flask import Flask

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Display 'Hello HBNB!' on the root route."""
    return 'Hello HBNB!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
