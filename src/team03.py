from collections import Counter
from nltk.tokenize import word_tokenize
import nltk
import os
import re

file = open("englishcorpus.txt", encoding="utf8").read()
tokens = word_tokenize(file)
tokens_words = [word for word in tokens if word.isalnum()]
vocab = Counter(tokens_words)
N =sum(vocab.values())
term_list = vocab.most_common(18000)
