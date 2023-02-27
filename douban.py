# -*- coding= utf-8 -*-
# @Time : 2021/4/15 21:53
# @ : faker
# @File 4.15_8 level up.py
# @Software: PyCharm
import requests
from bs4 import BeautifulSoup
def get_movies():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36 Edg/89.0.774.76',
        'Host': 'movie.douban.com'
    }
    movie_list = []
    for i in range(0,10):
        link = 'https://movie.douban.com/top250?start='+str(i*25)
        r = requests.get(link,headers = headers)

        soup = BeautifulSoup(r.text,'lxml')
        div_list = soup.find_all('div',class_='hd')
        for each in div_list:
            movie = each.a.span.text.strip()
            movie_list.append(movie)
        # div_list2 = soup.find_all('div',class_='bd')
        # for each in div_list2:
        #     movie_list.append(each)
    return movie_list
movies = get_movies()
f = open('movie_name.txt','r+')
i = 1
for single in movies:
    f.write(str(i)+'.'+single+'\n')
    i += 1
f.close()


