#!/usr/bin/python3
"""importing_Flask to_run the web_app"""
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.teardown_appcontext
def close(self):
    """ Method_to_close the_session """
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """shows_a html page_with states_and_cities"""
    states = storage.all(State)
    return render_template('8-cities_by_states.html', states=states)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000")
