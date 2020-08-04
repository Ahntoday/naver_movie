import requests
from bs4 import BeautifulSoup

URL = "https://movie.naver.com/movie/running/current.nhn"
response = requests.get(URL)

soup = BeautifulSoup(response.text, "html.parser")


movie_list = soup.select(
    '#content > .article > .obj_section > .lst_wrap > ul > li'
)


movie_data = []
for movie in movie_list:
    a_tag = movie.select_one('dl > dt > a')
    a_title = a_tag.contents[0]
    movie_link = a_tag['href']
    movie_link = movie_link.split("?code=")[1]
    movie_dict = {
        "title" : a_title,
        "link" : movie_link
    }
    movie_data.append(movie_dict)

print(movie_data)