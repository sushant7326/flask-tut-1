from app import app
from flask import render_template

@app.route("/")
def index():
    return render_template("public/index.html")

@app.route("/about")
def about():
    return render_template("public/about.html")

@app.route("/another")
def another():
    return "<h1 style='color:blue'>I dont know I forgot more dialogues!!!</h1>"