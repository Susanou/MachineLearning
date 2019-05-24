#!/usr/bin/env python3

#  Copyright (c) 2019, Cameron Hochberg
#  All rights reserved.
#
# Author: Cameron Hochberg
# Date: 05/2019
# Homepage: https://github.com/Susanou
# Email: cam.hochberg@gmail.com
#

from string import punctuation

import configparser
import math, os, sys, time
import itertools
import mysql.connector

def  count_word(word: str, freq: dict):
    """
    Fonction pour compter le nombre d'occurence d'un mot dans un texte donne
        :param word:str: le mot en question
        :param freq:dict: le dictionnaire utilise pour stocke les mots deja rencontres
    """

    print("[+] Counting frequency of %s" % word)

    if word in freq.keys():
        freq[word] += 1
    else:
        freq[word] = 1

    return freq


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

    print("[+] Removing determinants")

    determinants = [
        "le", "la", "les", "de", "des", "un", "une",
        "ce", "cet", "cette", "ces",
        "mon", "ma", "mes", "ton", "ta", "tes", "son", "sa", "ses",
        "notre", "votre", "leur", "nos", "vos", "leurs"
    ]
    for x in line:
        if x in determinants:
            line.remove(x)
    return line

def remove_punctuation(txt: str):
    """Fonction pour enlever la ponctuation d'un texte
    
    Parameters
    ----------
    txt : str
        texte a modifier

    Returns
    -------
    str
        Renvoi le texte sans ponctuation
    """
    print("[+] Removing punctuation")

    txt = txt.translate(str.maketrans('', '', punctuation))
    txt = txt.rstrip()

    return (''.join(e for e in txt if (e.isalnum() or e == ' '))).lower()
        

def radical(word: str):
    """Fonction pour enlever les terminaisons des mots et ne garder que les radicaux
    
    Parameters
    ----------
    word : str
        mot a stripper
    
    Returns
    -------
    str
        Renvoi le radical du mot
    """

    print('[+] removing radical of %s' % word)

    length = len(word)
    new = list(word)

    # enlever le genre de la fin du mot
    if word[length-1] == 'e' and length != 1:
        new.remove(word[length-1])
        print("[-] Removing feminine")

    if word[length-1] == 's' and length != 1:
        new.remove(word[length-1])
        print("[-] Removing plural")
        if word[length-2] =='e':
            new.remove(word[length-2])
            print("[-] Removing Feminine")
            
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

    print("[+] Accessing DB")

    config = configparser.ConfigParser()
    config.read('config.ini')

    db = mysql.connector.connect(
        host=config['mysqlDB']['host'],
        user=config['mysqlDB']['user'],
        passwd=config['mysqlDB']['pass'],
        db=config['mysqlDB']['db']
    )
    
    cursor = db.cursor()

    cursor.execute("SELECT * FROM Themes where nom='%s'" % theme)
    result = cursor.fetchone()

    if result == None:
        print("[+] Inserting theme %s into DB" % theme)
        cursor.execute("INSERT INTO `Themes` (nom) VALUES ('%s')" % theme)

    for mot, freq in freq.items():

        # query for frequence of a word within the theme given
        cursor.execute("SELECT word.id, word.mot, Themes.id, frequences.mot FROM word, frequences, Themes WHERE word.mot = '%s' AND frequences.mot = word.id AND Themes.nom ='%s' AND frequences.theme=Themes.id" % (mot, theme))
        result2 = cursor.fetchone()



        # check that the word doesn't already have a frequence  associated with it
        if result2 == None:

            print("[+] Inserting word %s into DB" % mot)
            cursor.execute("INSERT INTO `word` (mot) VALUES ('%s')" % mot)
            db.commit()

            print("[+] Inserting the frequency %d of word %s of theme %s in DB" % (freq, mot, theme))
            cursor.execute("INSERT INTO `frequences` (mot, theme, frequence) VALUES ((SELECT id FROM word WHERE mot = '%s'), (SELECT id FROM Themes WHERE nom = '%s'), %d)" % (mot, theme, freq))

            db.commit()

        # If it already has a frequency and already exists only update the frequency within the theme
        else:

            print("[+] Updating frequency of word %s" % mot)
            cursor.execute("UPDATE frequences SET frequence = frequence + %d where mot = (SELECT id FROM word WHERE mot = '%s')" % (freq, mot))
            db.commit()


    cursor.close()
    db.close()

def loading_animation(n):
    """Function to animate de waiting time
    """
    animation = "|/-\\"


    sys.stdout.write("\r[+] Loading " + animation[n % len(animation)])
    sys.stdout.flush()
    time.sleep(0.5)

    return n%len(animation)+1