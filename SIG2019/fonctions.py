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

    print("\033[1;32;40m[+] \033[0m Counting frequency of '%s'" % word)

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

    print("\033[1;31;40m[-] \033[0m Removing determinants")

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
    print("\033[1;31;40m[-] \033[0m Removing punctuation")

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

    print('\033[1;31;40m[-] \033[0m removing radical of \'%s\'' % word)

    length = len(word)
    new = list(word)

    # enlever le genre de la fin du mot
    if word[length-1] == 'e' and length != 1:
        new.remove(word[length-1])
        print("\033[1;31;40m[-] \033[0m Removing feminine")

    if word[length-1] == 's' and length != 1:
        new.remove(word[length-1])
        print("\033[1;31;40m[-] \033[0m Removing plural")
        if word[length-2] =='e':
            new.remove(word[length-2])
            print("\033[1;31;40m[-] \033[0m Removing Feminine")
            
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

    db = connectDB()
    
    cursor = db.cursor()

    cursor.execute("SELECT * FROM themes where nom='%s'" % theme)
    result = cursor.fetchone()

    if result == None:
        print("\033[1;32;40m[+] \033[0m Inserting theme '%s' into DB" % theme)
        cursor.execute("INSERT INTO `themes` (nom) VALUES ('%s')" % theme)

    for mot, freq in freq.items():

        # Query for already existing words
        cursor.execute("SELECT * FROM word WHERE mot='%s'" % mot)
        result2 = cursor.fetchone()

        # query for frequence of a word within the theme given
        query_result3=(
            """
            SELECT word.id, word.mot, themes.id, frequences.mot 
            FROM word, frequences, themes 
            WHERE word.mot = '%s' AND frequences.mot = word.id 
                AND themes.nom ='%s' AND frequences.theme=themes.id
            """
        )
        cursor.execute(query_result3, (mot, theme))
        result3 = cursor.fetchone()


        if result2 != None and result3 == None:
            print("\033[1;32;40m[+] \033[0m Inserting the frequency %d of word '%s' of theme '%s' in DB" % (freq, mot, theme))
            query = (
                """
                INSERT INTO `frequences` (mot, theme, frequence)
                VALUES (
                    (SELECT id FROM word WHERE mot = '%s'),
                    (SELECT id FROM themes WHERE nom = '%s'),
                     %d
                )
                """
            )
            cursor.execute(query, (mot, theme, freq))
            db.commit()
        
        # check that the word doesn't already have a frequence  associated with it
        elif result2 == None and result3 == None:

            print("\033[1;32;40m[+] \033[0m Inserting word '%s' into DB" % mot)
            cursor.execute("INSERT INTO `word` (mot) VALUES ('%s')" % mot)
            db.commit()

            print("\033[1;32;40m[+] \033[0m Inserting the frequency %d of word '%s' of theme '%s' in DB" % (freq, mot, theme))
            query = (
                """
                INSERT INTO `frequences` (mot, theme, frequence)
                VALUES (
                    (SELECT id FROM word WHERE mot = '%s'),
                    (SELECT id FROM themes WHERE nom = '%s'),
                     %d
                )
                """
            )
            cursor.execute(query, (mot, theme, freq))
            db.commit()

        # If it already has a frequency and already exists only update the frequency within the theme
        else:

            print("\033[1;32;40m[+] \033[0m Updating frequency of word '%s' in theme '%s'" % (mot, theme))
            query=(
                """
                UPDATE frequences SET frequence = frequence + %d 
                WHERE mot = (SELECT id FROM word WHERE mot = '%s') 
                AND theme = (SELECT id FROM themes WHERE nom = '%s')
                """
            )
            cursor.execute(query, (freq, mot, theme))
            db.commit()


    cursor.close()
    db.close()

def connectDB():
    """Fonction utilisee pour se connecter a la base de donnee
    
    Returns
    -------
    mysql.connector
        database object to use for cursor and commits
    """

    print("\033[1;32;40m[+] \033[0m Accessing DB")

    config = configparser.ConfigParser()
    config.read('config.ini')

    db = mysql.connector.connect(
        host=config['mysqlDB']['host'],
        user=config['mysqlDB']['user'],
        passwd=config['mysqlDB']['pass'],
        db=config['mysqlDB']['db']
    )
    
    return db

def get_frequence(word:str, theme:str):
    """Fonction permettant de recuperer la frequence d'un mot dans la base de donnee
    
    Parameters
    ----------
    word : str
        Mot dont on veut la frequence
    theme : str
        Theme d'ou on veut la frequence

    Returns
    -------
    int
        Returns the frequency of the word given
    """
    
    db = connectDB()
    
    cursor = db.cursor()

    occurence_query = ("""
        SELECT frequence FROM frequences
        where frequences.mot=(select id from word where mot=%s)
        and frequences.theme=(select id from themes where nom=%s)
        
        """)

    cursor.execute(occurence_query, (word, theme))
    freq = cursor.fetchone()[0]

    total_query = ("""
        SELECT n from total
        WHERE  Theme=%s
    """)
    cursor.execute(total_query, (theme))
    total = cursor.fetchone()[0]

    return freq/total, total

def interval(word:str, theme:str):
    """Fonction permettant de calculer l'interval de confiance
        pour un mot en fonction du theme
    
    Parameters
    ----------
    word : str
        mot dont on veut calculer l'intervalle de confiance
    theme : str
        theme associer au mot et a l'interval en question

    """
    
    freq, total = get_frequence(word, theme)

    bottom = freq - 1.96*math.sqrt(freq*(1-freq)/total)
    top = freq + 1.96*math.sqrt(freq*(1-freq)/total)

    db = connectDB()
    cursor = db.cursor()

    query=(
        """
        SELECT id FROM intervals 
        WHERE mot=(SELECT id FROM word WHERE mot='%s') 
        AND theme=(SELECT id FROM themes WHERE nom='%s')
        """
    )

    cursor.execute(query, (bottom, top, word, theme))
    result = cursor.fetchone()

    if result == None:
        insert_query =(
        """
            INSERT INTO `intervals` (bottom, top, mot, theme) VALUES
            (
                %d,
                %d,
                (SELECT id FROM word WHERE mot='%s'),
                (SELECT id FROM themes WHERE nom='%s')
            )
        """)

        cursor.execute(insert_query, (bottom, top, word, theme))
        db.commit()
    else:
        update_query=(
            """
            UPDATE intervals SET top = %d, bottom = %d
            WHERE mot=(SELECT id FROM word WHERE mot='%s') AND
            theme=(SELECT id FROM themes WHERE nom='%s')
            """
        )

        cursor.execute(update_query, (bottom, top, word, theme))
        db.commit()



def loading_animation(n):
    """Function to animate de waiting time
    """
    animation = "|/-\\"


    sys.stdout.write("\r[+] Loading " + animation[n % len(animation)])
    sys.stdout.flush()
    time.sleep(0.5)

    return n%len(animation)+1