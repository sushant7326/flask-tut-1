from flask import Flask

app = Flask(__name__)

@app.route("/")
def inde():
    return "This is NOT a power of your creation!!!"

if __name__ == "__main__":
    app.run()