import requests
import nltk
from bs4 import BeautifulSoup

# Preliminary download of stopwords
nltk.download('stopwords')

# Importing from Project Gutenberg and initial encoding
r = requests.get('http://www.gutenberg.org/cache/epub/30/pg30-images.html')
r.encoding = 'utf-8'
html = r.text
# Test the file by viewing the first 1000 characters
print(html[0:1000])

# Processing with bs4
soup = BeautifulSoup(html)
text = soup.get_text()

# Performing another print test to confirm.
print(text[3000:5000])

# Creating a tokenizer
tokenizer = nltk.tokenize.RegexpTokenizer('\w+')
tokens = tokenizer.tokenize(text)
print(tokens[0:10])

# Iterating over list to standardize capitalization
words = []

for word in tokens:
    words.append(word.lower())

# Printing out the first 10 words / tokens
print(words[0:8])

# Getting and configuring words to ignore (stop words)
sw = nltk.corpus.stopwords.words('english')

words_ns = []
for word in words:
    if word not in sw:
        words_ns.append(word)

# Printing the first 5 words_ns to check that stop words are gone
print(words_ns[0:10])

# Creating and plotting the word frequency distribution
freqdist = nltk.FreqDist(words_ns)
most_common = freqdist.max()
freqdist.plot(50, title='Most common words in KJV of The Bible')
print('The most common word in the KJV of The Bible is ' + most_common)