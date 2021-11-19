from collections import Counter
import nltk
from nltk.tokenize import word_tokenize
import re
from textblob import TextBlob

def irish_file_read():
    file = open("irish_corpus.txt", encoding="utf8").read()
    tokens = word_tokenize(file)
    tokens_words = [word for word in tokens if word.isalnum()]
    vocab = Counter(tokens_words)
    return vocab

def english_file_read():
    file = open("english_corpus.txt", encoding="utf8").read()
    tokens = word_tokenize(file)
    tokens_words = [word for word in tokens if word.isalnum()]
    vocab = Counter(tokens_words)
    return vocab
    
def detect_language(text):
    text_language = TextBlob(text)
    language = text_language.detect_language()
    return language
    
def english_word_suggestions(word):
    english_term_list = english_file_read()
    english_suggestions = []
    if (word.isalnum() == False):
         return word
    else:
        if (len(word)<=4):
            for key,value in english_term_list.items():
                edit = nltk.edit_distance(word, key)
                if (edit == 1):
                    english_suggestions.append(key)
            return english_suggestions
        else:
            if (5<=len(word)<=12):
                for key,value in english_term_list.items():
                    edit = nltk.edit_distance(word, key)
                    if (edit == 1 or edit == 2):
                        english_suggestions.append(key)              
                return english_suggestions 
                
def irish_word_suggestions(word):
    irish_term_list = irish_file_read()
    irish_suggestions = []
    if (word.isalnum() == False):
         return word
    else:    
        if (len(word)<=4):
            for key,value in irish_term_list.items():
                edit = nltk.edit_distance(word, key)
                if (edit == 1):
                    irish_suggestions.append(key)
            return irish_suggestions
        else:
            if (5<=len(word)<=12):
                for key,value in irish_term_list.items():
                    edit = nltk.edit_distance(word, key)
                    if (edit == 1 or edit == 2):
                        irish_suggestions.append(key)              
                return irish_suggestions
    
def spellCheck(text):
    language = detect_language(text)
    words = text.split()
    if (language != 'ga'):
        for i in words:
            return english_word_suggestions(i)
    else:
        for i in words:
            return irish_word_suggestions(i)
