#!/usr/bin/python3 

from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer
from nltk.tokenize import word_tokenize, sent_tokenize, WordPunctTokenizer
from os.path import isfile, join

import nltk
import os, sys, time
import string
import argparse # needed only if made into a script

def clean_text(file: str, lang: str, type: int):
    """Function to clean the text of an input file

    Parameters
    ----------
    file : str
        path to the file to be cleaned
    lang : str
        language the file is in 
        ie: 'french' to use the FrenchStemmer 'arabic' for ArabicStemmer
    type : int
        type of tokenisation:
        0: word tokenisation
        1: sentence tokenisation
        2: word and punctuation tokenisation

    Returns
    -------
    list
        returns a list containing all the words tokenized
    """    
    
    words = []

    try:
        f = open(file, "r")     # open the file in reading mode
        if f.mode == 'r':
            content = f.readlines()
            stemmer = SnowballStemmer(lang)

            for line in content:            # clean each line in the file

                line = line.maketrans('', '', string.punctuation)
                stemmed = []
                tokens = []
                if type == 0:
                    tokens = word_tokenize(line)
                    tokens = [w.lower() for w in tokens]
                    stemmed = [stemmer.stem(stem) for stem in tokens if stem not in stopwords.words(lang)]
                elif type == 2:
                    tokens = WordPunctTokenizer().tokenize(line)
                    stemmed = [stemmer.stem(stem) for stem in tokens if stem not in stopwords.words(lang)]

                words.extend(stemmed)
        
        f.close()
    except IOError:
        print("No file with that name was found\n")
    finally:
        return words