#!/usr/bin/env python3

#  Copyright (c) 2019, Cameron Hochberg
#  All rights reserved.
#
# Author: Cameron Hochberg
# Date: 05/2019
# Homepage: https://github.com/Susanou
# Email: cam.hochberg@gmail.com
#

import math, os, sys, time
import itertools
import mysql.connector

def  count_word(word: str, freq: dict):
    """
    Fonction pour compter le nombre d'occurence d'un mot dans un texte donne
        :param word:str: le mot en question
        :param freq:dict: le dictionnaire utilise pour stocke les mots deja rencontres
    """

    if word in freq.keys:
        freq[word] += 1
    else:
        freq[word] = 1

def remove_determinant(line: list):
    """Fonction pour enlever les determinants du texte
    
    Parameters
    ----------
    line : list
        Liste de mots d'une ligne du text
    
    Returns
    -------
    list
        Renvoi la liste de mots sans les determinants
    """

    determinants = [
        "le", "la", "les", "de", "des", "un", "une",
        "ce", "cet", "cette", "ces",
        "mon", "ma", "mes", "ton", "ta", "tes", "son", "sa", "ses",
        "notre", "votre", "leur", "nos", "vos", "leurs"
    ]
    for x in line:
        if x in determinants:
            x = None
        


    return line

def remove_punctuation(txt: str):
    """Fonction pour enlever la ponctuation d'un texte
    
    Parameters
    ----------
    txt : str
        texte a modifier
    """

    if '.' in txt:
        txt.replace('.', "")
    if ',' in txt:
        txt.replace(',', "")
    if '?' in txt:
        txt.replace('?', "")
    if '!' in txt:
        txt.replace('!', "")
        

def radical(word: str):
    """
    Fonction pour ne retenir que le radical du mot et eviter les problemes
    lies au genre et au nombre d'un mot
        :param word:str: le mot a coupe
for x in line:
        if '.' in x:
            x.replace('.', "")
        if ',' in x:
            x.replace(',', "")
        :returns: renvoi le radical suppose du mot
    """
    length = len(word)
    new = list(word)

    # enlever le genre de la fin du mot
    if word[length-1] == 'e' and length != 1:
        new[length-1] = None

    if word[length-1] == 's' and length != 1:
        new[length-1] = None
        if word[length-2] =='e':
            new[length-2] = None

    

    # maybe truncate more than that?
    

    return "".join(new)

def insert_db(freq: dict, theme: str):
    """Fonction permettant d'inserer les donnees dans la base de donnees
    
    Parameters
    ----------
    freq : dict
        Dictionnaire des mots et de leur frequence associee
    theme : str
        Nom du theme associer
    """
    db = mysql.connector.connect(
        host="localhost",
        user="fukurou",
        passwd="C4mer0n28oa",
        database="SIG",
    )

    cursor = db.cursor()

    cursor.execute("SELECT * FROM Themes where nom=%s", theme)

    if cursor != None:
        cursor.execute("INSERT INTO `Themes` (nom) VALUES (%s)", theme)

    for mot, freq in freq.items:
        cursor.execute("INSERT INTO `word` (mot) VALUES ('%s')", mot)
        db.commit()

        cursor.execute("INSERT INTO `frequences` (mot, theme, frequence) VALUES ((SELECT id FROM word where mot = %s), (SELECT id FROM Themes where nom = %s), %d)", mot, theme, freq)

        db.commit()


    # remember to add a line to terminate the connection.
    # LIVE CONNECTION ==> DANGER


def loading_animation(n):
    """Function to animate de waiting time
    """
    animation = "|/-\\"


    sys.stdout.write("\r Loading " + animation[n % len(animation)])
    sys.stdout.flush()
    time.sleep(0.5)

    return n%len(animation)+1