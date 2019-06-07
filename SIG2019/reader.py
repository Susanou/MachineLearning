#!/usr/bin/env python3

#  Copyright (c) 2019, Cameron Hochberg
#  All rights reserved.
#
# Author: Cameron Hochberg
# Date: 05/2019
# Homepage: https://github.com/Susanou
# Email: cam.hochberg@gmail.com
#

from multiprocessing import Pool
from os.path import isfile, join
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer
from nltk.tokenize import word_tokenize

import nltk
import sys, time, os
import fonctions_reader as fonctions

def read(file: str, theme: str, cluster: str):
    """Fonction pour lire le fichier texte
    
    Parameters
    ----------
    file : str  
        Nom du fichier a lire
    theme : str
        Nom du theme analyse
    cluster: str
        Nom du cluster associer
    """

    frequences = dict()     # dictionnaire [mots] = frequences
    try:
        f = open(file, "r")     # open the file in reading mode
        if f.mode == 'r':
            content = f.readlines()
            french_stemmer = SnowballStemmer('french')
            # while there is still something to read
            for line in content:
                line = word_tokenize(line, 'french')
                for word in line:
                    if word != "":
                        if word.isalnum():
                            if word not in stopwords.words('french'):
                                frequences = fonctions.count_word(french_stemmer.stem(word), frequences)
                
            fonctions.insert_db(frequences, theme, cluster)
        
        f.close()
    except IOError:
        print("No file with that name was found\n")
    finally:
        return 1
        

def main(argv):
    
    if argv == None:
        print("usage reader.py <fileName> <themeName>\n")
        return 0

    if argv[0] == "-h" or argv[0] == "help":
        print("usage reader.py <fileName> <themeName>\n")
        return 0

    if argv[0] == "-a" and argv[1] != None:
        for x in os.listdir(argv[1]):
            theme = x.split(".")
            cluster = theme[0].split("-")
            if isfile(join(argv[1], x)):
                read(join(argv[1], x), theme[0], cluster[0])    
    else:
        read(argv[0], argv[1])

if __name__ == "__main__":
    main(sys.argv[1:])