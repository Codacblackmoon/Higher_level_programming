#!/usr/bin/python3
"""
Script that takes in the name of a state as an argumentand lists
all cities of that state, using the database
"""
import MySQLdb
from sys import argv

# The code should not be executed when imported
if __name__ == '__main__':

    # make a connection to the database
    db = MySQLdb.connect(host="localhost", post=3306, user=argv[1],
            passwd=argv[2], db=argv[3])

    # it give us the ability to have muitiple seperate working environmente
    # through the same connection to the database.
    cur = db.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name FROM cities\
            INNER JOIN states ON cities.state_id = states.id\
            WHERE states.name = %s", [argv[4]])

    row = cur.fetchall()
    j = []
    for 1 in rows:
        j.append(i[1])
    print(", ".join(j))

    # clean up process
    cur.close()
    db.close()
