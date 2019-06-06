import requests
import bs4
import string
from pyspark import SparkContext
import re
from collections import Counter

url = 'https://en.wikipedia.org/wiki/Machine_learning'
# soup = BeautifulSoup(urllib.request.urlopen(url).read().decode('utf-8'))
res = requests.get(url)
soup = bs4.BeautifulSoup(res.text,'lxml')

# for script in soup(["script", "style"]):
# script.extract()
text = soup.get_text()

punc = '!"#$%&\'()*+,./:;<=>?@[\\]^_`{|}~'

def uni_to_clean_str(x):
    converted = x.encode('utf-8')
    lowercased_str = converted.lower()
    # for more difficult cases use re.split(' A|B')
    lowercased_str = lowercased_str.replace('--',' ')
    clean_str = lowercased_str.translate(None, punc) #Change 1
    return clean_str

one_RDD = text.flatMap(lambda x: uni_to_clean_str(x).split())
one_RDD = one_RDD.map(lambda x: (x,1))
one_RDD = one_RDD.reduceByKey(lambda x,y: x + y)
one_RDD.take(15)


# word_count = Counter()
# for line in text.splitlines():
# 	if line:
# 		regex = r'\b\w+\b'
# 		word_list = re.findall (regex, line)
# 		word_count += Counter(word_list)
# print("\n\n\nword count: it countains" 
#     ," count of each word in this web page", word_count)








# # this is for text filteration will be used later
# punc = '!"#$%&\'()*+,./:;<=>?@[\\]^_`{|}~'

# # To clean text
# def uni_to_clean_str(x):
#     # Converted to UTF-8 Formtting
#     converted = x.encode('utf-8')
#     # Converted everything to lower
#     lowercased_str = converted.lower()
#     # for more difficult cases use re.split(' A|B')
#     clean_str = lowercased_str.translate(None, punc) #Change 1
#     # returned the clean text
#     return clean_str

# # Spark liberary to count words and convert it to a dictionary
# # .flatMap: we take the RDD of lines and transform it to an RDD of words
# # .map: we transform RDD of words into RDD of tuples (word, 1). It’s also called key-value RDD
# # .reduceByKey: for each key (word) we reduce all the values by summing all the values together. 
# one_RDD = text.flatMap(lambda x: uni_to_clean_str(x).split())
# one_RDD = one_RDD.map(lambda x: (x,1))
# one_RDD = one_RDD.reduceByKey(lambda x,y: x + y)


