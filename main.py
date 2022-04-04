import flask
from flask import Flask

app = Flask(__name__)

@app.route("/")
def welcome():
    return "<h1>Hello</h1>"

@app.route("/contact")
def contact():
    return flask.render_template("contact.html")

@app.route("/home")
def home():
    return "Home"

@app.route("/gallery")
def gallary():
    return "Gallery"

if __name__ == "__main__":
    app.run()