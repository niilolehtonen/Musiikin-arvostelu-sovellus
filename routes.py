from app import app
from flask import render_template, request, redirect
import users
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

@app.route("/songs", methods = ["get","post"])
def songs():
    if request.method == "GET":
        return render_template("songs.html")
    if request.method == "POST":
        song_name = request.form['song_name']
        album_name = request.form['album_name']
        artist_name = request.form['artist_name']
        year = int(request.form['year'])
        rating = int(request.form['rating'])
        comment = request.form['comment']
        user_id = users.user_id()

    db.session.execute(text("""INSERT INTO songs (name, artist)
                 VALUES (:song_name, :artist_name)"""),
                 params={"song_name": song_name, "artist_name": artist_name})
    db.session.execute(text("""INSERT INTO albums (name, year)
                 VALUES (:album_name, :year)"""),
                 params={"album_name": album_name, "year": year})
    db.session.execute(text("""INSERT INTO artists (name)
                VALUES (:artist_name)"""),
                 params={"artist_name": artist_name})
    db.session.execute(text("""INSERT INTO reviews (song_name, rating, comment, user_id)
                VALUES (:song_name, :rating, :comment, :user_id)"""),
                 params={"song_name": song_name, "rating": rating, "comment": comment, "user_id": user_id})
    db.session.commit()
    return redirect("/songs")


@app.route("/albums", methods = ["get"])
def albums():
    return render_template("albums.html")