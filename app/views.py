from app import app
from flask import render_template

@app.route("/")
def index():
    return render_template("public/index.html")

@app.route("/about")
def about():
    return "<h1 style='color:red'>True art is an EXPLOSION!!!</h1>"

@app.route("/another")
def another():
    return "<h1 style='color:blue'>I dont know I forgot more dialogues!!!</h1>"