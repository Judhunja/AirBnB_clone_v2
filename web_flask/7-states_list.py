#!/usr/bin/python3
""" This script starts a web application and uses
storage for fetching data from the storage engine """
from models import storage
from sqlalchemy.orm import Session
from flask import Flask, render_template
from models.state import State


app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def states_list():
    """ Displays html page with a list of states """
    st = storage.all(State)
    return render_template("7-states_list.html", states=st)


@app.teardown_appcontext
def teardown(request):
    """ Removes the current SQLAlchemy Session after each
    request """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
