#!/usr/bin/env python3

import mysql.connector
import sys, time
import configparser

def test(theme: str):

    config = configparser.ConfigParser()
    config.read('config.ini')

    host=config['mysqlDB']['host'],
    user=config['mysqlDB']['user'],
    password=config['mysqlDB']['pass'],
    database=config['mysqlDB']['db']

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
    

if __name__ == "__main__":
    test("test")


def loading_animation(n):
    """Function to animate de waiting time
    """
    animation = "|/-\\"


    sys.stdout.write("\r[+] Loading " + animation[n % len(animation)])
    sys.stdout.flush()
    time.sleep(0.5)

    return n%len(animation)+1
