#!/usr/bin/python3
""" script that starts a Flask web application"""
from models import storage
from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.teardown_appcontext
def appcontext_teardown(exc=None):
    """ script that starts a Flask web application"""
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def conditional_templating(n=None):
    """ script that starts a Flask web application"""
    states = storage.all("State")
    data = {}
    return render_template('8-cities_by_states.html',
                           states=storage.all("State"))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
