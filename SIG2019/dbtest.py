import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="fukurou",
    passwd="C4mer0n28oa",
    database="SIG",
    )

cursor = db.cursor()

cursor.execute("SELECT * from word where id = 5")

cursor.fetchall()

if cursor != None:
    print("rien ici")
else:
    print("Il y a qqc")