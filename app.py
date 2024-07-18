from flask import Flask
from config import Config
from models import db, Movie
import csv

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)

    with app.app_context():
        db.create_all()
        read_csv_and_insert_data()

    from routes.main import main_bp
    app.register_blueprint(main_bp)

    return app

def read_csv_and_insert_data():
    db.session.query(Movie).delete()  # Limpa todos os registros existentes
    with open('database/movielist.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';')  # Usa ';' como delimitador
        for row in reader:
            movie = Movie(
                year=row['year'],
                title=row['title'],
                studios=row['studios'],
                producers=row['producers'],
                winner=row['winner']
            )
            db.session.add(movie)
        db.session.commit()

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
