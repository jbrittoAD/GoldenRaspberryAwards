from models import Movie
from collections import defaultdict

def get_producers_with_intervals(session):
    producers = defaultdict(list)
    movies = session.query(Movie).filter_by(winner='yes').all()

    for movie in movies:
        for producer in movie.producers.split(', '):
            producers[producer].append(movie.year)

    intervals = {"min": [], "max": []}
    min_interval = float('inf')
    max_interval = float('-inf')

    for producer, years in producers.items():
        if len(years) > 1:
            years.sort()
            intervals_producer = [
                {"interval": y2 - y1, "previousWin": y1, "followingWin": y2}
                for y1, y2 in zip(years, years[1:])
            ]
            for interval in intervals_producer:
                if interval["interval"] < min_interval:
                    min_interval = interval["interval"]
                    intervals["min"] = [{
                        "producer": producer,
                        **interval
                    }]
                elif interval["interval"] == min_interval:
                    intervals["min"].append({
                        "producer": producer,
                        **interval
                    })
                if interval["interval"] > max_interval:
                    max_interval = interval["interval"]
                    intervals["max"] = [{
                        "producer": producer,
                        **interval
                    }]
                elif interval["interval"] == max_interval:
                    intervals["max"].append({
                        "producer": producer,
                        **interval
                    })

    return intervals
