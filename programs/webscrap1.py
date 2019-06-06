# BeautifulSoup
# Request
import requests
import bs4
import re

res = requests.get('https://en.wikipedia.org/wiki/Machine_learning')
type(res)
#print(res.text)
soup = bs4.BeautifulSoup(res.text,'lxml')

def title():
    title= soup.select('title')
    print(title)
    print(title[0])
    print(title[0].getText())
# title()

def topic():
    topic = soup.select('.mw-headline')
    #if you want to select an ID
    #topic = soup.select('#mw-headline')
    #print(topic)
    for i in soup.select('.mw-headline'):
        print(i.text)
#topic()

models = soup.select('#Models')




