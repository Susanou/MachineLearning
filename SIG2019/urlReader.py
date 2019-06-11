#!/usr/bin/env python3

#  Copyright (c) 2019, Cameron Hochberg
#  All rights reserved.
#
# Author: Cameron Hochberg
# Date: 05/2019
# Homepage: https://github.com/Susanou
# Email: cam.hochberg@gmail.com
#

from bs4 import BeautifulSoup
from nltk.corpus import stopwords
from multiprocessing import Pool
from os.path import isfile, join
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer
from nltk.tokenize import word_tokenize

import nltk
import sys, time, os
import MachineLearning.SIG2019.fonctions_reader as fonctions
import urllib.request
import nltk

def get_page(url: str):
    """Fonction pour recuperer le texte nettoyer d'une page html
    
    Parameters
    ----------
    url : str
        Url de la page
    
    Returns
    -------
    str
        Renvoi le texte de la page sans le code HTML
    """
    response = urllib.request.urlopen(url)
    html = response.read()
    soup = BeautifulSoup(html, "html5lib")
    text = soup.get_text(strip=True)

    return text

def read_page(url: str, theme: str, cluster: str):
    """Fonction pour lire une page HTML et pousse son contenu dans la DB
    
    Parameters
    ----------
    url : str
        URL de la page
    theme : str
        Theme de la page
    cluster : str
        Cluster auquel apprtient la page
    """
    text = get_page(url)
    french_stemmer = SnowballStemmer('french')

    frequences = dict()

    text = word_tokenize(text, language='french')

    for word in text:
        if word == "":
            if word.isalnum():
                if word not in stopwords.words('french'):
                    frequences = fonctions.count_word(french_stemmer.stem(word), frequences)
    
    fonctions.insert_db(frequences, theme, cluster)

    db = fonctions.connectDB()
    cursor = db.cursor()

    cursor.execute("UPDATE url SET flag=1 WHERE url='%s'" % url)

    cursor.close()
    db.close()

    return 1

def get_unprocessed_url():
    """Fonctions permettant de recuperer toutes les urls non lues
    
    Returns
    -------
    list
        Renvoi une liste des urls non lues
    """
    db = fonctions.connectDB()
    cursor = db.cursor()

    cursor.execute("SELECT url FROM url WHERE flag=0")
    urls = cursor.fetchall()
    
    cursor.close()
    db.close()

    return urls

def get_all_url():
    """Fonctions permettant de recuperer toutes les urls
    
    Returns
    -------
    list
        Renvoi une liste des urls non lues
    """
    db = fonctions.connectDB()
    cursor = db.cursor()

    cursor.execute("SELECT url FROM url WHERE flag")
    urls = cursor.fetchall()
    
    cursor.close()
    db.close()

    return urls

def main(argv):
    if argv == None or argv[0]=="-h" or "help" in argv[0]:
        print("")

    if argv[0]=='-u':
        pass # get the unprocessed urls
    
    if argv[0]=='-a' or argv[0]=='--all':
        pass # get all urls regardless of flag


if __name__ == "__main__":
    main(sys.argv[1:])