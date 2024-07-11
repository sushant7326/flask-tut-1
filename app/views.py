from app import app
from flask import render_template, request, redirect, jsonify, make_response
from datetime import datetime
import os
from werkzeug.utils import secure_filename

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

@app.route("/sign-up", methods=["GET", "POST"])
def sign_up():

    if request.method=="POST":
        req = request.form
        username = req["username"]
        email = req.get("email")
        # password = request.form.get("password")
        password = request.form["password"]

        print(username, email, password)
        return redirect(request.url)

    return render_template("public/sign_up.html")

users = {
    "mitsuhiko": {
        "name": "Ayush Raj",
        "bio": "ML Engineer",
        "linkedin": "@daadhiwala"
    },
    "gvanrossum": {
        "name": "Aryan Sinha",
        "bio": "Electronics Engineer",
        "linkedin": "@as"
    },
    "elonmusk": {
        "name": "Sushant Singh",
        "bio": "Software Engineer",
        "linkedin": "@sushibouy"
    }
}

@app.route("/profile/<username>")
def profile(username):
    user = None
    if username in users:
        user = users[username]
    return render_template("public/profile.html", username=username, user=user)

@app.route("/multiple/<foo>/<bar>/<baz>")
def multi(foo, bar, baz):
    return f"foo is {foo}, bar is {bar}, baz is {baz}"

@app.route("/json", methods=["GET","POST"])
def json():
    # for POST request
    if request.method=="POST":
        # if POST request sent as JSON
        if request.is_json:
            # get the entire POST request as json
            req = request.get_json()
            # create a variable for the response return
            response = {
                "message": "JSON recieved!",
                # get the name from the POST request to return it
                "name": req.get("name")
            }
            # JSONify the response variable and return it with the status code
            res = make_response(jsonify(response), 200)
            return res
        # if POST request not sent as JSON
        else:
            res = make_response(jsonify({"message": "No JSON recieved!"}), 400)
            return res 
    # for GET request (default: this is what works when URL is put in the browser)
    else:
        return "Phuck auph"
    
@app.route("/guestbook")
def guestbook():
    return render_template("public/guestbook.html")

@app.route("/guestbook/create-entry", methods=["POST"])
def create_entry():
    if request.is_json:
        req = request.get_json()
        print(req)
        res = make_response(req, 200)
        return res
    else:
        res = make_response(jsonify({"message": "No JSON recieved!"}), 400)
        return res
    
# Query Strings
@app.route("/query")
def query():
    # if request.args:
    #     args = request.args
    #     serialized = ", ".join(f"{k}: {v}" for k,v in args.items())
    #     return f"(Query) {serialized}", 200

    # return "Query recieved!", 200

    print(request.query_string)

    return "No query string", 200

app.config["IMAGE_UPLOADS"] = "/home/sushant/comding/flask-tut-1/app/static/img/uploads"
app.config["ALLOWED_IMAGE_EXTENSIONS"] = ["PNG", "JPG", "JPEG", "GIF"]
app.config["MAX_IMAGE_FILESIZE"] = 0.5 * 1024 * 1024

def allowed_image(filename):
    if not "." in filename:
        return False
    
    ext = filename.rsplit(".",1)[1]

    if ext.upper() in app.config["ALLOWED_IMAGE_EXTENSIONS"]:
        return True
    else:
        return False
    
def allowed_image_filesize(filesize):
    if int(filesize) <= app.config["MAX_IMAGE_FILESIZE"]:
        return True
    else:
        return False
    
@app.route("/upload-image", methods=["GET", "POST"])
def upload_image():
    if request.method == "POST":
        if request.files:
            if not allowed_image_filesize(request.cookies.get("filesize")):
                print("Maximum File Size Exceeded")
                return redirect(request.url)
            image = request.files["image"]
            if image.filename == "":
                print("Image must have a filename")
                return redirect(request.url)
            
            if not allowed_image(image.filename):
                print("Invalid File Extension")
                return redirect(request.url)
            else:
                filename = secure_filename(image.filename)
                image.save(os.path.join(app.config["IMAGE_UPLOADS"], filename))

            print("Image Saved")
            return redirect(request.url)
    return render_template("public/upload_image.html")