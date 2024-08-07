#!/usr/bin/python3
""" This code search for the instance where state name is the same
    as argument 3"""
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
        cur.execute("""SELECT * FROM states
                       WHERE name like BINARY '{}'
                       ORDER BY states.id;
                    """.format(sys.argv[4]))

        rows = cur.fetchall()
        for row in rows:
            print(row)

    cur.close()
    db.close()
