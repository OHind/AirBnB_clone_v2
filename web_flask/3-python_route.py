#!/usr/bin/python3
from flask import Flask
"""web flasks"""


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """web flask"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def display_hbnb():
    """web flask"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def display_C(text):
    """web flask"""
    return 'C %s' % text.replace('_', ' ')


@app.route('/python', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def display_python(text):
    """web flask"""
    return 'Python %s' % text.replace('_', ' ')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
