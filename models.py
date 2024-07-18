from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Movie(db.Model):
    __tablename__ = 'movies'

    id = db.Column(db.Integer, primary_key=True, index=True)
    year = db.Column(db.Integer, index=True)
    title = db.Column(db.String, index=True)
    studios = db.Column(db.String, index=True)
    producers = db.Column(db.String, index=True)
    winner = db.Column(db.String, index=True)
