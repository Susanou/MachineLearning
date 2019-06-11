#!/usr/bin/env python3

import mysql.connector
import sys, time
import configparser
import fonctions_reader as fonctions

def test(theme: str):

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

    print(result)
    
    print("\033[0;37;40m Normal text\n")
    print("\033[2;37;40m Underlined text\033[0;37;40m \n")
    print("\033[1;37;40m Bright Colour\033[0;37;40m \n")
    print("\033[3;37;40m Negative Colour\033[0;37;40m \n")
    print("\033[5;37;40m Negative Colour\033[0;37;40m\n")
    
    print("\033[1;37;40m \033[2;37:40m TextColour BlackBackground          TextColour GreyBackground                WhiteText ColouredBackground\033[0;37;40m\n")
    print("\033[1;30;40m Dark Gray      \033[0m 1;30;40m            \033[0;30;47m Black      \033[0m 0;30;47m               \033[0;37;41m Black      \033[0m 0;37;41m")
    print("\033[1;31;40m Bright Red     \033[0m 1;31;40m            \033[0;31;47m Red        \033[0m 0;31;47m               \033[0;37;42m Black      \033[0m 0;37;42m")
    print("\033[1;32;40m Bright Green   \033[0m 1;32;40m            \033[0;32;47m Green      \033[0m 0;32;47m               \033[0;37;43m Black      \033[0m 0;37;43m")
    print("\033[1;33;40m Yellow         \033[0m 1;33;40m            \033[0;33;47m Brown      \033[0m 0;33;47m               \033[0;37;44m Black      \033[0m 0;37;44m")
    print("\033[1;34;40m Bright Blue    \033[0m 1;34;40m            \033[0;34;47m Blue       \033[0m 0;34;47m               \033[0;37;45m Black      \033[0m 0;37;45m")
    print("\033[1;35;40m Bright Magenta \033[0m 1;35;40m            \033[0;35;47m Magenta    \033[0m 0;35;47m               \033[0;37;46m Black      \033[0m 0;37;46m")
    print("\033[1;36;40m Bright Cyan    \033[0m 1;36;40m            \033[0;36;47m Cyan       \033[0m 0;36;47m               \033[0;37;47m Black      \033[0m 0;37;47m")
    print("\033[1;37;40m White          \033[0m 1;37;40m            \033[0;37;40m Light Grey \033[0m 0;37;40m               \033[0;37;48m Black      \033[0m 0;37;48m")

def loading_animation(n):
    """Function to animate de waiting time
    """
    animation = "|/-\\"


    sys.stdout.write("\r[+] Loading " + animation[n % len(animation)])
    sys.stdout.flush()
    time.sleep(0.5)

    return n%len(animation)+1

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

def query_test(word: str, theme: str):
    db = connectDB()
    
    cursor = db.cursor()

    occurence_query = ("""
        SELECT frequence FROM frequences
        where frequences.mot=(select id from word where mot=%s)
        and frequences.theme=(select id from themes where nom=%s )
        
        """)

    cursor.execute(occurence_query, (word, theme))
    freq = cursor.fetchone()[0]

    string = ("%s")

    print(string % (theme))

    total_query = ("""
        select n from total
        where theme='%s'
    """)
    cursor.execute(total_query % theme)
    total = cursor.fetchone()[0]

    print(freq)
    print(total)

    print("resultat= ", freq/total)

    return freq/total, total

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

    cursor.execute("SELECT url, cluster FROM url")
    urls = cursor.fetchall()
    
    cursor.close()
    db.close()

    return urls

if __name__ == "__main__":
    test = get_all_url()
    print(test)
    print(test[0])
