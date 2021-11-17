from collections import Counter
import nltk;
from nltk.tokenize import word_tokenize
import os
import re

from flask import Flask, redirect, url_for, render_template, request
app = Flask(__name__)

import re # Regular Expressions
from collections import Counter
import string
from flask import Flask, render_template, request

file = open("frequent_english_3000.txt")
term_list = {}
for line in file:
    key, value = line.split()
    term_list[key] = value

    
def edit_distance1(word):
    suggestions = []
    for key,value in term_list.items():
        edit = nltk.edit_distance(word, key)
        if (edit == 1):
            suggestions.append(key)
    print("mispelled words are:", word)
    print("possible corrections are:", suggestions)
    return suggestions
        
def edit_distance2(word):
   suggestions = []
   for key,value in term_list.items():
       edit = nltk.edit_distance(word, key)
       if (edit == 1 or edit == 2):
            suggestions.append(key)
   print("mispelled words are:", word)
   print("possible corrections are:", suggestions)
   return suggestions


def spellCheck(text):
    s=""
    words = text.split()
    for i in words:
        if i not in term_list:
            word_length = len(i)
            if (word_length <= 4):
                s=edit_distance1(i)
            else:
                s=edit_distance2(i)
    return s


@app.route('/', methods=['POST'])
def check():
    if request.method == 'POST':
        p=request.form.getlist('word')
        print(p)
        textoutput = spellCheck(p[0])
        print(textoutput)
        listToStr = ' '.join([str(element) for element in textoutput])
        print("listToStr : ", listToStr)
        print(listToStr)
        return listToStr
    

@app.route('/')
def index():
    return render_template("team03.html")

if __name__ == '__main__':
    app.run()