#!/usr/bin/env python3

import mysql.connector

def test(theme: str):
    db = mysql.connector.connect(
        host="localhost",
        user="fukurou",
        passwd="C4mer0n28oa",
        database="SIG",
    )
    
    cursor = db.cursor()

    cursor.execute("SELECT * FROM Themes where nom='%s'" % theme)
    result = cursor.fetchone()
    

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
