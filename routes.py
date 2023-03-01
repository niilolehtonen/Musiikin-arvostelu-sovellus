from app import app
from flask import render_template, request, redirect
import users
from db import db
from sqlalchemy.sql import text
from regex_check import regex_check 

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
    if request.method == "GET":
        result = db.session.execute(text("""
                SELECT a.name as artist_name, AVG(v.rating) as average_rating
                FROM artists a
                JOIN artist_releases ar ON a.id = ar.artist_id
                JOIN releases r ON ar.release_id = r.id
                JOIN (
                    SELECT song_name, rating
                    FROM reviews
                ) v ON r.song = v.song_name
                GROUP BY a.name;
        """))
        artist_info = result.fetchall()
        return render_template("artists.html", artist_info=artist_info)

@app.route("/releases", methods=["GET", "POST"])
def releases():
    if request.method == "GET":
        result = db.session.execute(text("""
            SELECT r.song, r.artist, r.album, r.year, AVG(v.rating) as average_rating
            FROM releases r
            LEFT JOIN reviews v ON r.song = v.song_name
            GROUP BY r.song, r.artist, r.album, r.year
            """))
        release_info = result.fetchall()
        return render_template("releases.html", release_info=release_info)
    if request.method == "POST":
        users.check_csrf()
        song_name = request.form["song_name"]
        if regex_check(song_name) == False:
            return render_template("error.html", message="Empty song name")
        if len(song_name) > 50:
            return render_template("error.html", message="Song name too long")
        album_name = request.form["album_name"]
        if regex_check(album_name) == False:
            return render_template("error.html", message="Empty album name")
        if len(album_name) > 50:
            return render_template("error.html", message="Album name too long")
        artist_name = request.form["artist_name"]
        if regex_check(artist_name) == False:
            return render_template("error.html", message="Empty artist name")
        if len(artist_name) > 50:
            return render_template("error.html", message="Artist name too long")
        year = (request.form["year"])
        if year.isdigit() == False:
            return render_template("error.html",message="Provide a valid year")
        if int(year) < 1 or int(year) > 2023:
            return render_template("error.html",message="Provide a valid year")  
        int(year) 
        db.session.execute(text("""
            INSERT INTO releases (song, artist, album, year)
            VALUES (:song_name, :artist_name, :album_name, :year)
            """), {"song_name": song_name, "artist_name": artist_name, "album_name": album_name, "year": year})
        
        artist_result = db.session.execute(text("""
            SELECT id FROM artists WHERE name = :artist_name
            """), {"artist_name": artist_name})
        
        artist_row = artist_result.fetchone()
        if artist_row is None:
            db.session.execute(text("""
                INSERT INTO artists (name) VALUES (:artist_name)
                """), {"artist_name": artist_name})
            artist_id = db.session.execute(text("""
                SELECT id FROM artists WHERE name = :artist_name
                """), {"artist_name": artist_name}).fetchone()[0]
        else:
            artist_id = artist_row[0]
        release_id = db.session.execute(text("""
            SELECT id FROM releases WHERE song = :song_name AND artist = :artist_name AND album = :album_name
            """), {"song_name": song_name, "artist_name": artist_name, "album_name": album_name}).fetchone()[0]

        db.session.execute(text("""
            INSERT INTO artist_releases (artist_id, release_id) VALUES (:artist_id, :release_id)
            """), {"artist_id": artist_id, "release_id": release_id})
        
        db.session.commit()
        
        return redirect("/releases")


@app.route("/review/<song_name>", methods = ["get","post"])
def review(song_name):
    if request.method == "GET":
        result = db.session.execute(text("""SELECT rating, comment, u.name FROM reviews JOIN users u ON user_id = u.id WHERE :song_name = song_name """), params={"song_name": song_name})
        reviews = result.fetchall()
        return render_template("review.html",reviews=reviews, song_name=song_name)
    if request.method == "POST":
        users.check_csrf()
        rating = request.form['rating']
        if not rating.isdigit() or int(rating) not in [1,2,3,4,5]:
            return render_template("error.html",message="Provide a rating (1, 2, 3, 4 or 5)")
        comment = request.form['comment']
        if regex_check(comment) == False:
            return render_template("error.html",message="Provide a comment")
        if len(comment) > 50:
            return render_template("error.html",message="Comment too long")
        user_id = users.user_id()
        db.session.execute(text("""INSERT INTO reviews (song_name, rating, comment, user_id) VALUES (:song_name, :rating, :comment, :user_id)"""),params={"song_name": song_name, "rating": rating, "comment": comment, "user_id": user_id})
        db.session.commit()
        return redirect(f"/review/{song_name}")