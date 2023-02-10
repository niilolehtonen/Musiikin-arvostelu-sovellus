from db import db
from flask import session
from sqlalchemy.sql import text

def names():
    #ql = cursor.execute(text("""SELECT * FROM artists"""))
    result = db.session.execute(text("""SELECT * FROM artists"""))
    return result.fetchall()