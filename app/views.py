from app import app
from flask import render_template
from datetime import datetime

@app.template_filter("clean_date")
def clean_date(dt):
    return dt.strftime("%d %b %Y")

@app.route("/")
def index():
    return render_template("public/index.html")

@app.route("/about")
def about():
    return render_template("public/about.html")

@app.route("/jinja")
def jinja():
    my_name = "Sushant"
    age = 21
    langs = ["python", "javascript", "bash", "c++"]
    friends = {
        "DW":21,
        "Piyutuz":22,
        "As":20,
        "BBC":23,
        "Bhikhari":21,
        "Kuttwa":22
    }
    colors = ("Red", "Green")
    cool = True

    class GitRemote:
        def __init__(self, name, creator, description, url):
            self.name = name
            self.creator = creator
            self.description = description
            self.url = url
        
        def pull(self):
            return f"Pulling repo \"{self.name}\" by {self.creator}"
        
        def clone(self):
            return f"Cloning into {self.url}"
        
    my_remote = GitRemote(
        name="Flask Jinja",
        creator="Julian Nash",
        description="Template design tutorial",
        url="http://github.com/sushant7326/jinja.git"
    )
        
    def repeat(x,qty):
        return x * qty
    
    date = datetime.now()

    my_html = "<h1>True art is an EXPLOSION!!!<h1>"

    suspicious = "<script>alert('You expected a hacker, but it was ME, DIO-da!!!')</script>"

    return render_template("public/jinja.html",
                           my_name = my_name,
                           age = age,
                           langs = langs,
                           friends = friends,
                           colors = colors,
                           cool = cool,
                           GitRemote = GitRemote,
                           my_remote=my_remote,
                           repeat = repeat,
                           date = date,
                           my_html = my_html,
                           suspicious = suspicious
                           ) 

@app.route("/another")
def another():
    return "<h1 style='color:blue'>I dont know I forgot more dialogues!!!</h1>"