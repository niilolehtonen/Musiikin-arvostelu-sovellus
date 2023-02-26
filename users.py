from db import db
from flask import session, request, abort
from werkzeug.security import check_password_hash, generate_password_hash
from sqlalchemy.sql import text
import secrets

def login(name, password):
    sql = "SELECT name, password, id FROM users WHERE name=:name"
    result = db.session.execute(text(sql), {"name":name})
    user = result.fetchone()
    print(user)
    if not user:
        return False
    if not check_password_hash(user[1], password):
        return False
    session["user_id"] = user[2]
    session["user_name"] = name
    session["csrf_token"] = secrets.token_hex(16)
    return True

def logout():
    del session["user_id"]
    del session["user_name"]

def register(name, password):
    hash_value = generate_password_hash(password)
    try:
        sql = """INSERT INTO users (name, password)
                 VALUES (:name, :password)"""
        db.session.execute(text(sql), {"name":name, "password":hash_value})
        db.session.commit()
        return True
    except:
        return False

def user_id():
    return session.get("user_id", 0)

def check_csrf():
    if session["csrf_token"] != request.form["csrf_token"]:
        abort(403)