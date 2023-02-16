from flask import Flask, render_template, redirect, request
from users import User
app = Flask(__name__)
secret_key = "Secret lol."


@app.route("/")
def index():
    users = User.show_all()
    return render_template("read_all.html", users=users)


@app.route("/create_user", methods=["POST"])
def create_user():
    data = {
        "first_name": request.form["fname"],
        "last_name": request.form["lname"],
        "email": request.form["email"],
    }
    User.create_user(data)
    return redirect("/")


@app.route("/create_user/new")
def create_page():
    return render_template("create.html")


if __name__ == "__main__":
    app.run(debug=True, port=8001)
