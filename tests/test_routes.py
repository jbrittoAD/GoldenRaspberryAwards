import unittest
from app import create_app
from models import db, Movie

class TestRoutes(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

        with self.app.app_context():
            db.drop_all()
            db.create_all()
            self.populate_data()

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    def populate_data(self):
        movies = [
            Movie(year=2008, title="Movie 1", studios="Studio 1", producers="Producer 1", winner='yes'),
            Movie(year=2006, title="Movie 2", studios="Studio 2", producers="Producer 1", winner='yes'),
            Movie(year=2018, title="Movie 3", studios="Studio 3", producers="Producer 2", winner='yes'),
            Movie(year=2019, title="Movie 4", studios="Studio 4", producers="Producer 2", winner='yes'),
            Movie(year=1900, title="Movie 5", studios="Studio 5", producers="Producer 3", winner='yes'),
            Movie(year=1999, title="Movie 6", studios="Studio 6", producers="Producer 3", winner='yes'),
            Movie(year=2000, title="Movie 7", studios="Studio 7", producers="Producer 4", winner='yes'),
            Movie(year=2096, title="Movie 8", studios="Studio 8", producers="Producer 4", winner='yes')
        ]

        for movie in movies:
            db.session.add(movie)
        db.session.commit()

    def test_producers_intervals(self):
        response = self.client.get('/producers')
        self.assertEqual(response.status_code, 200)
        
        data = response.get_json()
        expected_intervals = {'max': [{'followingWin': 1999, 'interval': 99, 'previousWin': 1900, 'producer': 'Producer 3'}], 
                              'min': [{'followingWin': 2019, 'interval': 1, 'previousWin': 2018, 'producer': 'Producer 2'}]}
        self.assertEqual(data, expected_intervals)

if __name__ == '__main__':
    unittest.main()
