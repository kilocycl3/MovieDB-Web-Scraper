from bs4 import BeautifulSoup
import re

def get_soup(url):
    
    res = BeautifulSoup(url,'html.parser')
    
    return res


def movie_name(soup):
    
    movie_title = ''

    try:
    
        # movie_div = soup.find('div', class_='title')

        movie_title = soup.find('h2')

        movie_title = f'{movie_title.find("a").text} {movie_title.find("span").text}'
    
    except Exception as e:
        print("Error retrieving Movie name")
#         movie_title = "NA"

    return 'NA' if movie_title == '' else movie_title


def movie_ratings(soup):
    
    ratings = ''

    try:

        ratings = soup.find('div',class_='user_score_chart')['data-percent']

    except Exception as e:
        print("Error retrieving Movie ratings")
#         rating = "NA"

    return 'NA' if ratings == '' else ratings


def movie_genres(soup):
    
    genres = ''

    try:
        
        genres = soup.find('span',class_='genres').text
        # genres = genres.strip()

        genres = genres.split(',')
        genres = list(map(lambda a: a.strip()+',',genres))
        genres[-1] = genres[-1][:-1]
        genres = '\n'.join(genres)

    except Exception as e:
        print("Error retrieving Movie genre ")
#         genres = "NA"
        
    return 'NA' if genres == '' else genres


def movie_release_date(soup):

    release_date = ''    
    try:
        
        release_date = soup.find('span',class_='release').text

        release_date = release_date.strip()
        
        pattern = '\d{2}/\d{2}/\d{4}'

        release_date = re.findall(pattern,release_date)[0]
        
    except Exception as e:
        print("Error retrieving release date")
#         release = "NA"
        
    return 'NA' if release_date == '' else release_date


def movie_runtime(soup):

    runtime = ''
    try:
        runtime = soup.find('span', class_='runtime').text
        runtime = runtime.strip()

    except Exception as e:
        print("Error retrieving runtime")
#         runtime = "NA"
        
    return 'NA' if runtime == '' else runtime


def movie_director(soup):
    
    director = ''
    
    try:
        movie_cast = soup.find_all('li',class_='profile')
        for profile in movie_cast:

            work = profile.find('p',class_='character').text
            name = profile.find('a').text
            if work.count('Director')>0:
                director = name
                break
        
    except Exception as e:
        print("Error retrieving director")
        
#     else:
#         director = 'NA'
        
    return 'NA' if director == '' else director


