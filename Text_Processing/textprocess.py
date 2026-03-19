from nltk import word_tokenize,pos_tag, ne_chunk
from nltk.stem import PorterStemmer

porter = PorterStemmer()
sentence = """The world is a very beautiful place, but the world I want to create is not
        this. So lets just work harder for a new world"""



#Reading files 
file = open("a_text_file.txt", "r")
every_thing = ""
word = []
for ch in file:
    every_thing+=ch

every_thing = every_thing.lower()
tokens = word_tokenize(every_thing)
tags = pos_tag(tokens)
entities = ne_chunk(tags)
print(entities)
#Cleaning text
#Tokenization
#Basic NLP


#Task:
    #Load a text file, count words and find the most frequent words