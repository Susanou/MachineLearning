#!/usr/bin/env python3

import math, os
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

def remove_determinant(lines: list):
    for x in lines:
        if x == "le" or x == "la" or x == "les":
            x = None
        
        if x == "de" or x == "des":
            x = None
    
    return lines

def radical(word: str):
    """
    Fonction pour ne retenir que le radical du mot et eviter les problemes
    lies au genre et au nombre d'un mot
        :param word:str: le mot a coupe

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

def insert_db(freq: dict, theme: int):
    """
    Function pour inserer les valeurs obtenues dans la base de donnee
        :param freq:dict: dictionnaire obtenu apres avoir parouru le texte donne
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