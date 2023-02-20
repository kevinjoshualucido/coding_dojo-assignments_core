from flask import render_template, redirect, request
from flask_app import app
from flask_app.models.dojo import Dojo


@app.route("/")
def index():
    return redirect("/dojos")


@app.route("/dojos")
def all_dojos():
    return render_template("index.html", all_dojos=Dojo.get_all_dojos())


@app.route("/create/dojo", methods=["POST"])
def create_dojo():
    Dojo.save_dojo(request.form)
    return redirect("/dojos")


@app.route("/dojo/<int:id>")
def show_dojo(id):
    data = {"id": id}
    return render_template("dojos.html", dojo=Dojo.get_one_dojo_with_ninjas(data))