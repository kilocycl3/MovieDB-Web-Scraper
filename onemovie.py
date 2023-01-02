from page import *
from scraper import *
from sys import argv


res = get_url_data(argv[1])
soup = get_soup(res)
print(movie_name(soup))
print(movie_director(soup))
print(movie_genres(soup))
print(movie_ratings(soup))
print(movie_runtime(soup))