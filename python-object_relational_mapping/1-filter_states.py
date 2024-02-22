#!/usr/bin/python3

""" lists all states from the database hbtn_0e_usa """

import MySQLdb
import sys

if __name__ == "__main__":

    usrn = sys.argv[1]
    pswd = sys.argv[2]
    dtbs = sys.argv[3]

    db = MySQLdb.connect(host="localhost", user=usrn, passwd=pswd, db=dtbs)

    cursor = db.cursor()

    cur.execute("""SELECT * FROM states WHERE name
                LIKE BINARY 'N%' ORDER BY states.id""")

    for row in cursor.fetchall():
        print(row)

    cursor.close()
    db.close()

