#!/usr/bin/python3
"""
    takes in the name of a state as an argument and lists all cities of that
    state, using the database hbtn_0e_4_usa
"""
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = db.cursor()
    match = sys.argv[4]
    query = """
               SELECT cities.name FROM cities
               JOIN states
               ON states.id = cities.state_id
               WHERE states.name LIKE %s
            """
    cur.execute(query, (match, ))
    rows = cur.fetchall()
    tmp = list(row[0] for row in rows)
    print(*tmp, sep=", ")
    cur.close()
    db.close()
