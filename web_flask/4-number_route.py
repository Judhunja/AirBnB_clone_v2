#!/usr/bin/python3
""" This script configures a Flask web application with
three routes """
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    return "Hello HBNB"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_is_fun(text):
    text_spaces = text.replace("_", " ")
    return f"C {text_spaces}"


@app.route("/python/", defaults={"text": "is cool"}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def display_python(text):
    text_spaces = text.replace("_", " ")
    return f"Python {text_spaces}"


@app.route("/number/<int:n>", strict_slashes=False)
def number_if_int(n):
    if type(n) == int:
        return f"{n} is a number"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
