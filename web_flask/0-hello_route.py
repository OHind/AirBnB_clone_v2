#!/usr/bin/python3
"""flash web"""
from flask import Flask
"""flash web"""


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """flash web"""
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
