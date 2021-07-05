# Import libraries
import os
import numpy as np
import pandas as pd
import nltk
import gensim
from tqdm import tqdm
import re
import pyLDAvis
import pyLDAvis.gensim
import spacy


# Assign directory
directory_path = os.path.abspath("/Users/elliotdamasah/Documents/School/Thesis/NSA/Data1/pdfToText/Text-1/Text/2003")
# Select files in directory
data_path = [x for x in os.listdir(directory_path) if not x.startswith(".")]
# Show number of files in directory
len(data_path)


# Concatenate location to file names, creating absolute paths for all the files in the directory
def paths(directory_path):
    ret=[]
    for x in os.listdir(directory_path):
        if not x.startswith("."):
            ret.append(directory_path+"/"+x)
            ret.sort()
    return ret
full_directory = paths(directory_path)


# Read files from directory
def opener(xx):
    listers=[]
    for x in xx:
        r=open(x,"r")
        f=r.read()
        listers.append(f)
        r.close()
    return listers
read_text = opener(full_directory)


# Clean files (Setup for stopword, lemmatization, and tokenization)
stop_words = nltk.corpus.stopwords.words('english')
wtk = nltk.tokenize.RegexpTokenizer(r'\w+')
wnl = nltk.stem.wordnet.WordNetLemmatizer()
nlp = spacy.load('en_core_web_sm')
extend_stop_words = ["si","fouo","tsi","sid","sigint","nsa"]
[stop_words.append(x) for x in extend_stop_words]


# Function for cleaning
def cleaner1(read):
    cleaned_read_text1 = []
      for x in read:
        x = re.sub(r'\t|\n|\r|\x0b|\x0c|\s{2,100}', ' ', x)
        try:
            x = re.search(r'\d+\/\d+\/\d+\s*(.*)\s*\"\(U\/\/FOUO\)', x, re.MULTILINE | re.DOTALL);
            x = x.group(1)
        except:
            print('COULD NOT EXTRACT FILE AT INDEX: '+str(x))
            continue     
        cleaned_read_text1.append(x)
    return cleaned_read_text1
cleaner1(read_text)[1]


"""
ADJ	 adjective	big, old, green, incomprehensible, first
ADP	 adposition	in, to, during
ADV	 adverb	very, tomorrow, down, where, there
AUX	 auxiliary	is, has (done), will (do), should (do)
CONJ	conjunction	and, or, but
CCONJ	coordinating conjunction	and, or, but
DET	 determiner	a, an, the
INTJ	interjection	psst, ouch, bravo, hello
NOUN	noun	girl, cat, tree, air, beauty
NUM	 numeral	1, 2017, one, seventy-seven, IV, MMXIV
PART	particle	’s, not,
PRON	pronoun	I, you, he, she, myself, themselves, somebody
PROPN	proper noun	Mary, John, London, NATO, HBO
PUNCT	punctuation	., (, ), ?
SCONJ	subordinating conjunction	if, while, that
SYM	 symbol	$, %, §, ©, +, −, ×, ÷, =, :), 😝
VERB	verb	run, runs, running, eat, ate, eating
X	other	sfpksdpsxmsa
SPACE	space	
"""

def cleaner(read):
    cleaned_read_text = []
        for x in read:
        x = re.sub(r'\t|\n|\r|\x0b|\x0c|\s{2,100}', ' ', x)
        try:
            x = re.search(r'\d+\/\d+\/\d+\s*(.*)\s*\"\(U\/\/FOUO\)', x, re.MULTILINE | re.DOTALL);
            x = x.group(1)
        except:
            print('COULD NOT EXTRACT FILE AT INDEX')
            continue
        
        x = x.lower()
        x = [token.strip() for token in wtk.tokenize(x)]
        #x = [x.text for x in nlp(" ".join(x)) if x.pos_ not in ["NOUN","PRON"]] # Part of speech tagging that removes symbols, pronouns, auxillary verb, 
        x = [wnl.lemmatize(token) for token in x if not token.isnumeric()]
        x = [token for token in x if len(token) > 2]
        x = [token for token in x if token not in stop_words]
        x = list(filter(None, x))
        
        #norm_papers.append(paper_tokens)    
        cleaned_read_text.append(x)
        
        
# Phrase extraction -- bigram
norm_papers = cleaner(read_text)
# min_count ignores all words and bi-grams with total collected count lower than 20 across the corpus
# threshold is for the number of times a phrase would appear in the corpus before it qualifies as part of the bigram
bigram = gensim.models.Phrases(norm_papers, min_count=10, threshold=40, delimiter=b'_') # higher threshold fewer phrases.
bigram_model = gensim.models.phrases.Phraser(bigram)
    return cleaned_read_text
