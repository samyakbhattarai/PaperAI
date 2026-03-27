import re
from pathlib import Path

import matplotlib.pyplot as plt
import nltk
from nltk import ne_chunk, pos_tag, word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer


porter = PorterStemmer()

# Reading files
text_path = Path(__file__).resolve().parent / "a_text_file.txt"
if not text_path.exists():
    raise FileNotFoundError(f"Text file not found: {text_path}")

with open(text_path, "r", encoding="utf-8") as file:
    every_thing = file.read()

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

fdist.plot(10)
plt.show()


#Task:
    #Load a text file, count words and find the most frequent words