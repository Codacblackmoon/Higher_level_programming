#!/usr/bin/python3
"""
Script that list all cities all cities from the database hbtn_0e_4_usa
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
            ORDER BY cities.id ASC")

    row = cur.fetchall()
    for 1 in rows:
        print(i)
    # clean up process
    cur.close()
    db.close()
