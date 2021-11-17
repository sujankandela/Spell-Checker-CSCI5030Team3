from collections import Counter
import nltk;
from nltk.tokenize import word_tokenize
import re
from textblob import TextBlob

file = open("frequent_english_3500.txt")
term_list = {}
for line in file:
    key, value = line.split()
    term_list[key] = value
    
def detect_language(text):
    text_language = TextBlob(text)
    language = text_language.detect_language()
    return language
    
def edit_distance1(word):
    suggestions = []
    for key,value in term_list.items():
        edit = nltk.edit_distance(word, key)
        if (edit == 1):
            suggestions.append(key)
    print("mispelled words are:", word)
    print("possible corrections are:", suggestions)
        
def edit_distance2(word):
   suggestions = []
   for key,value in term_list.items():
       edit = nltk.edit_distance(word, key)
       if (edit == 1 or edit == 2):
            suggestions.append(key)
   print("mispelled words are:", word)
   print("possible corrections are:", suggestions)
   
def spellCheck(text):
    words = text.split()
    language = detect_language(text)
    for i in words:
        if i not in term_list:
            word_length = len(i)
            if (word_length <= 4):
                edit_distance1(i)
            else:
                edit_distance2(i)
