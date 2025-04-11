from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup


# try:
#     html = urlopen('http://pythonscraping.com/pages/page1.html')
# except HTTPError as e:
#     print(e)
# else:
#     bs = BeautifulSoup(html, 'html.parser')
#     try:
#         badContent = bs.nonExistingTag.anotherTag
#     except AttributeError as e:
#         print('Tag was not found')
#     else:
#         if badContent == None:
#             print ('Tag was not found')
#         else:
#             print(badContent)

def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    try:
        bs = BeautifulSoup(html.read(), 'html.parser')
        title = bs.body.h1
    except AttributeError as e:
        return None
    return title

title = getTitle('http://pythonscraping.com/pages/page1.html')
if title == None:
    print('Title could not be found')
else:
    print(title)