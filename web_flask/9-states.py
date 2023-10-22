#!/usr/bin/python3
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City

app = Flask(__name__)


@app.route("/states", strict_slashes=False)
def list_states():
    """ Display a list of all states """
    st = storage.all(State)
    return render_template("9-states.html",
                           states=st,
                           state=None,
                           state_not_found=False)


@app.route("/states/<id>", strict_slashes=False)
def list_cities(id):
    """ Display a specific state and its cities or 'Not found' """
    st = None
    cities = []

    for s in storage.all(State).values():
        if s.id == id:
            st = s
            cities = s.cities
            break

    state_not_found = st is None
    return render_template("9-states.html",
                           states=None,
                           state=st,
                           cities=cities,
                           state_not_found=state_not_found)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
