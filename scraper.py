from bs4 import BeautifulSoup
import re
from datetime import datetime

def get_soup(url):
    
    res = BeautifulSoup(url,'html.parser')
    
    return res


def movie_name(soup):
    
    movie_title = ''

    try:
    
        # movie_div = soup.find('div', class_='title')

        movie_title = soup.find('h2')

        movie_title = movie_title.find("a").text  # Get only title

        # movie_title = f'{movie_title.find("a").text} {movie_title.find("span").text}'  # Get Title with year
    
    except Exception as e:
        print("Movie title not found")
#         movie_title = "NA"

    return 'NA' if movie_title == '' else movie_title


def movie_ratings(soup):
    
    ratings = ''

    try:

        ratings = soup.find('div',class_='user_score_chart')['data-percent']

    except Exception as e:
        print("Movie ratings not found")
#         rating = "NA"

    return 'NA' if ratings == '' else ratings


def movie_genres(soup):
    
    genres = ''

    try:
        
        genres = soup.find('span',class_='genres').text

        genres = genres.split(',')  # Method 1
        genres = list(map(lambda a: a.strip(),genres))  # Method 1
        genres = ', '.join(genres)  # Method 1


        # genres = genres.split(',')  # Method 2
        # genres = list(map(lambda a: a.strip()+',',genres))  # Method 2
        # genres[-1] = genres[-1][:-1]  # Method 2
        # genres = '\n'.join(genres)  # Method 2

    except Exception as e:
        print("Movie genre not found")
#         genres = "NA"
        
    return 'NA' if genres == '' else genres


def movie_release_date(soup):

    release_date = ''    
    try:
        
        temp_date = soup.find('span',class_='release').text

        temp_date = temp_date.strip()
        
        pattern = '\d{2}/\d{2}/\d{4}'

        temp_date = re.findall(pattern,temp_date)[0]

        date = datetime.strptime(temp_date,'%m/%d/%Y')

        release_date = date.strftime('%m/%d/%Y')
        
    except Exception as e:
        print("Release date not found")
#         release = "NA"
        
    return 'NA' if release_date == '' else release_date


def movie_runtime(soup):

    runtime = ''
    try:
        runtime = soup.find('span', class_='runtime').text
        runtime = runtime.strip()

    except Exception as e:
        print("Runtime not found")
#         runtime = "NA"
        
    return 'NA' if runtime == '' else runtime


def movie_director(soup):
    
    director = []
    
    try:
        movie_cast = soup.find_all('li',class_='profile')
        for profile in movie_cast:

            work = profile.find('p',class_='character').text
            name = profile.find('a').text
            if work.count('Director')>0:
                director.append(name)
        
    except:
        pass

    if len(director)==0:
        print("Director name not found")
        director.append('NA')
    
    director = ', '.join(director)
    
    return director

    # return 'NA' if director == '' else director


