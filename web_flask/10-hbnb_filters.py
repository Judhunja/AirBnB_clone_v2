#!/usr/bin/python3
""" This script starts a web application and uses
storage for fetching data from the storage engine """
from models import storage
from flask import Flask, render_template
from models.state import State
from models.amenity import Amenity


app = Flask(__name__)


@app.route("/hbnb_filters", strict_slashes=False)
def states_list():
    """ Return a hbnb html page with states, cities and
    amenities """
    st = storage.all(State)
    amenities = storage.all(Amenity)
    return render_template("10-hbnb_filters.html", states=st, amenities=amenities)


@app.teardown_appcontext
def teardown(request):
    """ Removes the current SQLAlchemy Session after each
    request """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
