from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen('http://www.pythonscraping.com/pages/page3.html')

bs = BeautifulSoup(html, 'html.parser')

# print(bs.find('img', {'src': '../img/gifts/img1.jpg'}).parent.previous_sibling.get_text())

# images = bs.find_all('img',
#                      {'src': re.compile(r'\.\.\/img\/gifts/img.*\.jpg')})
# for image in images:
#     print(image['src'])

# imgs = bs.find_all('img', {'src': re.compile(r'\.\.\/img\/gifts/img.*\.jpg')})

# for img in imgs:
#     print(img.attrs['src'])

# Função Lambda
print(bs.find_all(lambda img: len(img.attrs) == 10))
