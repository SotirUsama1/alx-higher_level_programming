#!/usr/bin/python3
""" This is a script to display all the instances in a table from a
database """

import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(
                         host="localhost",
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3],
                         port=3306
    )

    cursor = db.cursor()

    cursor.execute("SELECT * FROM states;")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    db.close()
