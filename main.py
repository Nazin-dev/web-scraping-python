from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime
import random
import re


# for link in bs.find_all('a'):
#     if 'href' in link.attrs:
#         print(link.attrs['href'])

# for link in bs.find('div', {'id': 'bodyContent'}).find_all(
#     'a', href=re.compile(r'^(/wiki/)((?!:).)*$')):
#     if 'href' in link.attrs:
#         print(link.attrs['href'])

random.seed(datetime.datetime.now().timestamp())
def getLinks(url):
    html = urlopen(f'https://en.wikipedia.org{url}')
    bs = BeautifulSoup(html.read(), 'html.parser')
    return bs.find('div', {'id': 'bodyContent'}).find_all('a', href=re.compile(r'^(/wiki/)((?!:).)*$'))

links = getLinks('/wiki/Kevin_Bacon')
while len(links) > 0:
    newArticle = links[random.randint(0, len(links)-1)].attrs['href']
    print(newArticle)
    links = getLinks(newArticle)

