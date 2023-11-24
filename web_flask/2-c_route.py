#!/usr/bin/python3
"""script that starts a Flask web application"""

from flask import Flask


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_world():
    """script that starts a Flask web application"""
    return 'Hello HBNB!'


@app.route('/hbnb')
def hello():
    """script that starts a Flask web application"""
    return 'HBNB'


@app.route('/c/<text>')
def c_text(text):
    """script that starts a Flask web application"""
    text = text.replace('_', ' ')
    return 'C {}'.format(text)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
