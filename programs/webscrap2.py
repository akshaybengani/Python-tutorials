# imported the required modules for this task
import requests
import bs4

url = 'https://en.wikipedia.org/wiki/Machine_learning'
page = requests.get(url)
soup = bs4.BeautifulSoup(page.text,'lxml')
basepagecontent = soup.select('.mw-parser-output')
#print(basepagecontent)
data = soup.find('div',id="History_and_relationships_to_other_fields").p
print(data)