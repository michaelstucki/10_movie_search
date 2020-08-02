import requests
import collections

MovieResult = collections.namedtuple(
    'MovieResult',
    'imdb_code, title, director, keywords, duration, genres, rating, year, imdb_score')


def find_movies(search_text):
    if not search_text or not search_text.strip():
        raise ValueError("Search text is required")

    url = 'https://movieservice.talkpython.fm/api/search/{}'.format(
        search_text)

    resp = requests.get(url)
    resp.raise_for_status()

    movie_data = resp.json()
    movie_list = movie_data.get('hits')

    movies = [MovieResult(**movie_dict) for movie_dict in movie_list]

    movies.sort(key=lambda m: -m.year)

    return movies
