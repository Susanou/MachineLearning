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
import fonctions_reader as fonctions
import urllib.request
import nltk
import argparse

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
    response = urllib.request.urlopen("%s" % url)
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
        if word != "":
            if word.isalnum():
                if word not in stopwords.words('french'):
                    frequences = fonctions.count_word(french_stemmer.stem(word), frequences)
    
    fonctions.insert_db(frequences, theme, cluster)

    db = fonctions.connectDB()
    cursor = db.cursor()

    cursor.execute("UPDATE url SET flag=1 WHERE url='%s'" % url)
    db.commit()

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

    cursor.execute("SELECT url, cluster.nom FROM url JOIN cluster ON url.cluster=cluster.id WHERE flag=0")
    urls = cursor.fetchall()
    
    cursor.close()
    db.close()

    return urls

def get_all_url():
    """Fonction permettant d'obtenir toutes les URLs sans prendre en compte
    le flag
    
    Returns
    -------
    list
        Renvoi la liste des URLs
    """
    db = fonctions.connectDB()
    cursor = db.cursor()

    cursor.execute("SELECT url, cluster.nom FROM url JOIN cluster ON url.cluster=cluster.id")
    urls = cursor.fetchall()
    
    cursor.close()
    db.close()

    return urls

def get_cluster_url(cluster: int):
    """Fonctions permettant de recuperer toutes les urls d;un cluster donne
    
    Returns
    -------
    list
        Renvoi une liste des urls non lues
    """
    db = fonctions.connectDB()
    cursor = db.cursor()

    cursor.execute("SELECT url, cluster.nom FROM url, cluster WHERE cluster.id=%d" % cluster)
    urls = cursor.fetchall()
    
    cursor.close()
    db.close()

    return urls

def unprocessed():
    urls = get_unprocessed_url()

    for content in urls:

        url = content[0].split('/')
        read_page(content[0], url[-1], content[1])

    return 1

def all():
    urls = get_all_url()

    for content in urls:

        url = content[0].split('/')
        read_page(content[0], url[-1], content[1])

    return 1

def cluster(c: int):
    urls = get_cluster_url(c)

    for content in urls:
        url = content[0].split('/')
        read_page(content[0], url[-1], content[1])

    return 1

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Programm to create data from url texts')
    parser.add_argument('-a', '--all', action='store_true', help='Get all urls regardless of flag')
    parser.add_argument('-u', '--unprocessed', action='store_true', help='Get all unprocessed URLs')
    parser.add_argument('-c', '--cluster', type=int, default=0, nargs='?', help='Get all the urls related to input cluster')

    args = parser.parse_args()

    if args.all:
        print("getting all urls")
        all()
    elif args.unprocessed:
        print("getting unprocessed urls")
        unprocessed()
    else:
        print("getting url of cluster %d" % args.cluster)
        cluster(args.cluster)
    