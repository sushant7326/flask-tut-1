from app import app
from flask import render_template

@app.route("/admin/dashboard")
def admin_dasboard():
    return render_template("admin/dashboard.html")

@app.route("/admin/profile")
def admin_profile():
    return render_template("admin/profile.html")

@app.route("/admin/another")
def admin_another():
    return "<h1 style='color:blue'>Sushant: I dont know I forgot more dialogues!!!</h1>"