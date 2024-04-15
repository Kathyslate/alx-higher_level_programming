#!/usr/bin/python3
import MySQLdb

def list_states(username, password, db_name):
    db = MySQLdb.connect(host="localhost", user=username, passwd=password, db=db_name)
    cursor = db.cursor()
    cursor.execute("SELECT * FROM hbtn_0e_0_usa ORDER BY id ASC")
    results = cursor.fetchall()
    for row in results:
        print(row)
    cursor.close()
    db.close()
list_states('your_username', 'your_password', 'hbtn_0e_0_usa')
