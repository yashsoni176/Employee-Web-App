from flask import Flask

app = Flask(__name__)

@app.route("/")
def welcome():
    return "Welcome to my website"

@app.route("/contact")
def contact():
    return "Contact US"

@app.route("/home")
def home():
    return "Home"

@app.route("/gallery")
def gallary():
    return "Gallery"

if __name__ == "__main__":
    app.run()