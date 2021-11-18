from collections import Counter
from nltk.tokenize import word_tokenize
import nltk
from textblob import TextBlob
import re
import json

file = open("irish_corpus.txt", encoding="utf8").read()
tokens = word_tokenize(file)
tokens_words = [word for word in tokens if word.isalnum()]
vocab = Counter(tokens_words)
N = sum(vocab.values())


def edit_distance(word):
    irish_suggestions = []
    irish={}
    if (word.isalnum() == False):
         return word
    else:
        if word in vocab:
            return word
        else:
            if (len(word)<=4):
                for key,value in vocab.items():
                    edit = nltk.edit_distance(word, key)
                    if (edit == 1):
                        irish_suggestions.append(key)
                        irish[key] = value
                if (len(irish) > 1):
                    return max(irish, key=irish.get)
                else:
                    return irish
            else:
                if (5<=len(word)<=12):
                    for key,value in vocab.items():
                        edit = nltk.edit_distance(word, key)
                        if (edit == 1 or edit == 2):
                            irish_suggestions.append(key)
                            irish[key] = value
                    if (len(irish) > 1):
                        return max(irish, key=irish.get)
                    else:
                        return irish
                

if __name__=='__main__':
    listi = []
    dic = {}
    with open('input-test.txt',  encoding="utf8") as f:
        for row in f:
            stripped = row.strip()
            row_list = stripped.split()
            w = edit_distance(row_list[0])
            dic[row_list[0]] = w      
            with open('team_correction.tsv', "w", encoding="utf-8") as file:
                for k,v in dic.items():
                    file.write("{} {}\n".format(k,v))
            file.close()
    f.close()
