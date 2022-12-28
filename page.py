import requests
from scraper import *


def get_url_data(url):
    
    res = requests.get(url).text
    return res


# def get_url(url):

#     res = requests.get(url).url
    
#     return res


def get_page_list(url):
    
    lst = []
    
    for i in range(1,51):
        lst.append(f'{url}{i}')
        
    return lst


def get_movie_url_list(url_lst,main_url):

    movie_url_lst = []
    for url in url_lst:
        page = get_url_data(url)
        page_soup = get_soup(page)

        per_movie_url = page_soup.find_all('a', class_='image')

        for item in per_movie_url:

            temp_link = f'{main_url}{item["href"]}'

            # return_link = get_url(temp_link)

            movie_url_lst.append(temp_link)

    return movie_url_lst