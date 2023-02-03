from app import app
from flask import render_template, request, redirect
import users


@app.route("/")
def index():
    return render_template("frontpage.html")

@app.route("/login")
def login():

    username = request.form["username"]
    password = request.form["password"]

    if not users.login(username, password):
        return render_template("register_error.html", message="Wrong username or password")
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
        username = request.form["inputUsername"]
        if len(username) < 1 or len(username) > 20:
            return render_template("register_error.html", message="Username too long")
        password1 = request.form["Password1"]
        password2 = request.form["Password2"]
        if password1 != password2:
            return render_template("register_error.html", message="Passwords do not match")
        if password1 == "":
            return render_template("register_error.html", message="Empty password")
        if not users.register(username, password1):
            return render_template("register_error.html", message="Registration unsuccesful")
        return redirect("/")

        
        