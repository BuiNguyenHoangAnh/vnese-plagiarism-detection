import pickle
from nltk.lm import  WittenBellInterpolated
import pandas as pd

from utils import *

SOURCE = "../data/vie/_vie.json"
source_data = pd.read_json(SOURCE)[0]
n = 4

def ngram(document, n):
    doc = document.split()
    tmp = [] 
    sent_len = len(doc) - n +1
    for i in range(sent_len):
        tmp.append(doc[i : i+n]) 
    return tmp

def build_model(source, n):
    ngrams = []
    i = 0
    for doc in source:
        print(i)
        i += 1
        ngrams.append(ngram(doc, n))
    model = WittenBellInterpolated(n)
    model.fit(ngrams, vocabulary_text= source)
    print(model.vocab)
    with open('model_ngram', 'wb') as picklefile:
        pickle.dump(model, picklefile)

build_model(source_data, n)