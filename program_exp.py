# (toy) RESTful API
# https://movieservice.talkpython.fm/api/search/particle
# (real) www.omdbapi.com
# http://www.omdbapi.com/?t=hur
# $1.00/month

import requests
import collections

MovieResult = collections.namedtuple(
    'MovieResult',
    'imdb_code, title, director, keywords, duration, genres, rating, year, imdb_score')
search = input('Movie to search for: ')
url = 'https://movieservice.talkpython.fm/api/search/{}'.format(search)

resp = requests.get(url)
resp.raise_for_status()

movie_data = resp.json()
movie_list = movie_data.get('hits')

# movies = []
# for movie in movie_list:
#     movie = MovieResult(
#         imdb_code=movie.get('imdb_code'),
#         title=movie.get('title'),
#         director=movie.get('director'),
#         keywords=movie.get('keywords'),
#         duration=movie.get('duration'),
#         genres=movie.get('genres'),
#         rating=movie.get('rating', 0),
#         year=movie.get('year', 0),
#         imdb_score=movie.get('imdb_score', 0.0)
#     )
#     movies.append(movie)

# dict -> keyword arguments (KEYS MUST MATCH IDENTICALLY!)
# movies = []
# for movie_dict in movie_list:
#     movie = MovieResult(**movie_dict)  # apply dict as keyword arguments
#     movies.append(movie)

# list comprehension
movies = [MovieResult(**movie_dict) for movie_dict in movie_list]

print('Found {} movies for search "{}"'.format(len(movies), search))
for movie in movies:
    print("{} -- {}".format(movie.year, movie.title))
