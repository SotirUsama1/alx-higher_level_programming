#!/usr/bin/python3
""" This code prevent sql injection"""
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

    cur = db.cursor()

    if sys.argv[4]:
        arg = sys.argv[4].split("'")[0]
        print(arg)
        cur.execute("""SELECT * FROM states
                       WHERE name like BINARY '{}'
                       ORDER BY states.id;
                    """.format(arg))

        rows = cur.fetchall()
        for row in rows:
            print(row)

    cur.close()
    db.close()
