#!/usr/bin/python3
""" This code print states begin with letter N """
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

    cursor.execute("""SELECT * FROM states
                      WHERE name LIKE BINARY 'N%'
                      ORDER BY states.id;
                   """)
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    db.close()
