from collections import Counter
import nltk;
from nltk.tokenize import word_tokenize
import re
from textblob import TextBlob

file = open("frequent_english_18000.txt")
english_term_list = {}
for line in file:
    key, value = line.split()
    english_term_list[key] = value
    
def detect_language(text):
    text_language = TextBlob(text)
    language = text_language.detect_language()
    return language
    
def english_edit_distance(word):
    english_suggestions = []
    if word not in english_term_list:
        if (len(word)<=4):
            for key,value in english_term_list.items():
                edit = nltk.edit_distance(word, key)
                if (edit == 1):
                    english_suggestions.append(key)
            print("mispelled words are:", word)
            print(english_suggestions)
        else:
            if (5<=len(word)<=12):
                for key,value in english_term_list.items():
                    if word not in english_term_list:
                        edit = nltk.edit_distance(word, key)
                        if (edit == 1 or edit == 2):
                            english_suggestions.append(key)
                print("mispelled words are:", word)
                print(english_suggestions)  
    
def spellCheck(text):
    language = detect_language(text)
    print(language)
    words = text.split()
    if (language != 'ga'):
        for i in words:
            english_edit_distance(i)
