from app import app
from flask import render_template, request, redirect
import users
from artistslist import names
from db import db
from sqlalchemy.sql import text

@app.route("/")
def index():
    return render_template("frontpage.html")

@app.route("/login", methods = ["get","post"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        #users.login(username,password)
        if not users.login(username, password):
            return render_template("error.html", message="Wrong username or password")
        return redirect("/")

@app.route("/logout")
def logout():
    users.logout()
    return redirect("/")

@app.route("/register", methods =["get","post"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    if request.method == "POST":
        username = request.form["username"]
        if len(username) < 1 or len(username) > 20:
            return render_template("error.html", message="Username too long")
        password1 = request.form["password1"]
        password2 = request.form["password2"]
        if password1 != password2:
            return render_template("error.html", message="Passwords do not match")
        if password1 == "":
            return render_template("error.html", message="Empty password")
        if not users.register(username, password1):
            return render_template("error.html", message="Registration unsuccesful")
        return redirect("/")

@app.route("/artists", methods = ["get"])
def artists():
    #artist_names = names()
    result = db.session.execute(text("""SELECT * FROM artists"""))
    artist_info = result.fetchall()
    return render_template("artists.html",artist_info=artist_info)

        
        