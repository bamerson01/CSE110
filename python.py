from urllib.request import Request, urlopen
import random

secret_word = ''

# SECRET WORD GENERATOR
# This will scrape content from a webpage and seperate the words into a list. We then select a random sample from the list to choose a secret word.
url = "http://www.mit.edu/~ecprice/wordlist.10000"
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()
page_content = webpage.decode('utf-8')
word_split = page_content.split("\n")
word_list = random.sample(word_split, 10)
for word in word_list:
    if len(word) > 4 and word.isalpha():
        secret_word = word.lower()
print(f'The secret word is {secret_word}')


# from urllib.request import Request, urlopen
# import random

# url = "http://www.columbia.edu/~fdc/sample.html"
# page = urlopen(url)
# html_bytes = page.read()
# webpage = html_bytes.decode("utf-8")
# first5 = webpage.split("\n")[:500]
# word_list = random.sample(first5, 6)
# print(word_list)
