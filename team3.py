from flask import *
import re
from collections import Counter
import string

def read_corpus(filename):
    with open(filename,'r') as file:
        lines=file.readlines()
        words=[]
        num=[]
        for line in lines:
            p=list(line.split())
            words.append(p[0])
            num.append(int(p[1]))
        total=sum(num)
        # for line in lines:
        #     words+=re.findall(r'\w+',line.lower())
        words.append(total)
    return words

def countWord(filename):
    with open(filename,'r') as file:
        lines=file.readlines()
        words=[]
        num=[]
        for line in lines:
            p=list(line.split())
            words.append(p[0])
            num.append(int(p[1]))
    return num
def split(word):
    return [(word[:i],word[i:]) for i in range(len(word)+1)]

def delete(word):
    return [l + r[1:] for l,r in split(word) if r]

def swap(word):
    return [l+r[1]+r[0]+r[2:] for l,r in split(word) if len(r)>1]

def replace(word):
    letters=string.ascii_lowercase
    return [l+c+r[1:] for l,r in split(word) if r for c in letters]

def insert(word):
    letters= string.ascii_lowercase
    return [l+c+r for l,r in split(word) for c in letters]

def level_one_edits(word):
    return set(delete(word)+swap(word)+replace(word)+insert(word))

def level_two_edits(word):
    return set(e2 for e1 in level_one_edits(word) for e2 in level_one_edits(e1))

def correct_spelling(word, vocabulary, word_probabilities):
    if word in vocabulary:
        print(f'{word} is already correctly spelt')
        return
    suggestion =level_one_edits(word) or level_two_edits(word) or [word]
    best_guess=[w for w in suggestion if w in vocabulary]
    return [(w,word_probabilities[w]) for w in best_guess]


app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])

def hm():
    r=""
    if request.method == 'POST':
        form = request.form
        r=home(form)
    return render_template("index1.html",result=r)

@app.route("/word.html")

def word():
    return render_templ
ate("word.html")

@app.route("/view",methods=['POST'])
def view():
    name=request.form.get('name')
    return name

@app.route("/res", methods=['POST'])

def home(x):
    words=read_corpus("./speller1.txt")
    total_word_count=words[-1]
    words=words[:-1]
    vocabs=set(words)
    words_count=countWord("./speller1.txt")
    k=0
    l=dict()
    for i in words:
        l[i]=words_count[k]
        k+=1
    #total_word_count=float(sum(words_count.values()))
    vocabs.add("how");
    word_prob={word: l[word]/total_word_count for word in l.keys()}
    word=x["message"]
    r=""
    word_list=list(word.split())
    
    for i in word_list:
        guess=correct_spelling(i.lower(),vocabs,word_prob)
        if guess:
            r=r+str(guess[0][0])
        else:
            r=r+i
        r=r+" "
    return r

if __name__=="__main__":
    app.run(debug=True)