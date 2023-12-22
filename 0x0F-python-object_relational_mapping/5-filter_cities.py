#!/usr/bin/python3
"""
Script that takes in the name of a state as an argument and lists
all cities of that state, using the database
"""
import MySQLdb
from sys import argv

# The code should not be executed when imported
if __name__ == '__main__':
    # make a connection to the database
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])

    cur = db.cursor()
    cur.execute("SELECT cities.id, cities.name FROM cities\
                INNER JOIN states ON cities.state_id = states.id\
                WHERE states.name = %s", [argv[4]])

    rows = cur.fetchall()
    a = []
    for n in rows:
        a.append(n[1])
    print(", ".join(a))

    # Clean up process
    cur.close()
    db.close()
