import requests as rq
from bs4 import BeautifulSoup

BUrl= 'https://books.toscrape.com/'

BHeader={
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36'
}

BResp = rq.get(url=BUrl, headers=BHeader)

BSoup = BeautifulSoup(BResp.content,'html.parser')

books = BSoup.find('div',attrs={'class':'h1'})

print(f'books={books}')

BookNames = BSoup.find_all('h3')

print('BookNames',BookNames)

BookTitle =[]

for Title in BookNames:
    print('Title', Title.find('a')['title'])
    
   # print('BookTitle',BookTitle)
    BookTitle.append(Title.find('a')['title'])

priceList = BSoup.find_all('p',attrs={'class':'price_color'})
for price in priceList:
    print('price',price.text)

RatingList = BSoup.find_all('p',attrs={'class':'star-rating'})
for rating in RatingList:
    print('rating',rating['class'][1])
