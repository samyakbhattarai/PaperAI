import nltk
from nltk.corpus import stopwords
from nltk import word_tokenize,pos_tag, ne_chunk
import re
from nltk.stem import PorterStemmer
import matplotlib.pyplot as plt

porter = PorterStemmer()
sentence = """The world is a very beautiful place, but the world I want to create is not
        this. So lets just work harder for a new world"""



#Reading files 
file = open("a_text_file.txt", "r")
every_thing = ""
word = []
for ch in file:
    every_thing+=ch

#Cleaning text

def clean_text(text: str) -> str:
    """Clean text using regex: lower-case, strip, remove non-alphanumeric except spaces."""
    text = text.lower().strip()
    # remove URLs, emails first (if present)
    text = re.sub(r'https?://\S+|www\.\S+', '', text)
    text = re.sub(r'\S+@\S+', '', text)
    # remove non-alphanumeric characters, keep spaces
    text = re.sub(r'[^a-z0-9\s]', ' ', text)
    # collapse whitespace
    text = re.sub(r'\s+', ' ', text)
    return text

every_thing = clean_text(every_thing)

tokens = word_tokenize(every_thing)

stop_words = set(stopwords.words('english'))
filtered = [word for word in tokens if word not in stop_words and word.isalpha()]

fdist = nltk.FreqDist(filtered)

print(fdist.most_common(5))

fdist.plot(10, title="most frequent")
plt.show()

#Basic NLP


#Task:
    #Load a text file, count words and find the most frequent words