#!/usr/bin/python3
"""Script that lists all ststes from the database hbtn_0e_0_usa"""
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
    cur.execute("SELECT * FROM states")

    row = cur.fetchall()
    for 1 in rows:
        print(i)
    # clean up process
    cur.close()
    db.close()
