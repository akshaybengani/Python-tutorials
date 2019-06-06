# Required liberaries
import requests
import bs4
import re
import string
from pyspark import SparkContext
from collections import Counter
import matplotlib.pyplot as plt

# The webpage URL to be scraped 
url = 'https://en.wikipedia.org/wiki/Machine_learning'

# request object containing page data
res = requests.get(url)

# soup to extract webpage data in form of text sorted with lxml format
soup = bs4.BeautifulSoup(res.text,'lxml')

# This contains all the text of full page
text = soup.get_text()

# Used Counter liberary insteed of PySpark since I dont have much time left right
# now to learn PySpark will update this code in next commit.

word_count = Counter()
for line in text.splitlines():
	if line:
		regex = r'\b\w+\b'
		word_list = re.findall (regex, line)
		word_count += Counter(word_list)
#print("\n\n\nWord count: it countains count of each word in this web page \n", word_count)

# Used Matplotlib to display graph 
plt.bar(range(len(word_count)), list(word_count.values()), align='center')
plt.xticks(range(len(word_count)), list(word_count.keys()))
plt.show()


