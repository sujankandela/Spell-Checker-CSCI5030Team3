from collections import Counter
import nltk;
from nltk.tokenize import word_tokenize
import re
from textblob import TextBlob

english_file = open("frequent_english_18000.txt")
irish_file = open("frequent_irish_3500.txt")
sum_of_english = 20941846    #this sum is computed from the english corpus used
sum_of_irish_words = 17302634 #this sum is computed from the irish corpus used

english_term_list = {}
irish_term_list ={}

for line in english_file:
    key, value = line.split()
    english_term_list[key] = value
    
for line in irish_file:
    key, value = line.split()
    irish_term_list[key] = value
    
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
                
def irish_edit_distance(word):
    irish_suggestions = []
    if word not in irish_term_list:
        if (len(word)<=4):
            for key,value in irish_term_list.items():
                edit = nltk.edit_distance(word, key)
                if (edit == 1):
                    irish_suggestions.append(key)
            print("mispelled words are:", word)
            print(irish_suggestions)
        else:
            if (5<=len(word)<=12):
                for key,value in irish_term_list.items():
                    if word not in irish_term_list:
                        edit = nltk.edit_distance(word, key)
                        if (edit == 1 or edit == 2):
                            irish_suggestions.append(key)
                print("mispelled words are:", word)
                print(irish_suggestions)
    
def spellCheck(text):
    language = detect_language(text)
    print(language)
    words = text.split()
    if (language != 'ga'):
        for i in words:
            english_edit_distance(i)
    else:
        for i in words:
            irish_edit_distance(i)
