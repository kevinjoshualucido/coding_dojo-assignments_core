from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "this is my secret key."


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/process", methods=["POST"])
def survey():
    print("Get Post Info")
    session["name"] = request.form["name"]
    session["location"] = request.form["location"]
    session["fav"] = request.form["fav"]
    session["comments"] = request.form["comments"]
    return render_template("result.html")


if __name__ == "__main__":
    app.run(debug=True, port=5007)
