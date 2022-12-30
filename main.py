from page import *
from scraper import *
from export import exportcsv
# import threading
# import time

def per_page_scrap():
    pass

def code():

    main_url = 'https://www.themoviedb.org'   
    page_url = 'https://www.themoviedb.org/movie?page='

    final_data = []

    page_url_lst = get_page_list(page_url)

    movie_url_lst = get_movie_url_list(page_url_lst,main_url)

    # threading.Thread()
    for count,url in enumerate(movie_url_lst):

        print(f'Current Movie Count: {count+1} Link: {url}')

        movie_info = {}
        # Get Movie Soup
        movie_page_data = get_url_data(url)
        movie_soup = get_soup(movie_page_data)

        # time.sleep(1)

        # movie_section = movie_soup.find('section',class_='header poster')
        
        # Get Movie Title
        movie_title = movie_name(movie_soup)
        # print(movie_title)

        # Get Movie Ratings
        ratings = movie_ratings(movie_soup)
        # print(ratings)

        # Get Movie Genres 
        genre = movie_genres(movie_soup)
        # print(genre)

        # Get Movie Release Date 
        release_date = movie_release_date(movie_soup)
        # print(release_date)

        # Get Movie Runtime 
        runtime = movie_runtime(movie_soup)
        # print(runtime)

        # Get Movie Director 
        director = movie_director(movie_soup)
        # print(director)

        movie_info = {
            'Name': movie_title,
            'Rating': ratings,
            'Genre': genre,
            'Release Date': release_date,
            'Runtime': runtime,
            'Director': director,
            'Url': url
        }
        
        final_data.append(movie_info)

        

    
    exportcsv(final_data)
    print("Done")


if __name__ == '__main__':

    code()