#!/usr/bin/python3
"""  lists all states from the database hbtn_0e_0_usa """
""" I am unsure why it has no permissions, when I did give u+x.. """
import MySQLdb
import sys


if __name__ == "__main__":
    try:
        with MySQLdb.connect(host="localhost", user=sys.argv[1],
                             passwd=sys.argv[2], db=sys.argv[3], port=3306) as db:
            with db.cursor() as cur:
                cur.execute("SELECT * FROM states")
                rows = cur.fetchall()
                for row in rows:
                    print(row)
    except MySQLdb.Error as e:
        print(f"Error {e.args[0]}: {e.args[1]}")
        sys.exit(1)
