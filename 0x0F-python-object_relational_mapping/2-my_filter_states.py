#!/usr/bin/python3
"""Script that take in an argument and displays all values in the states
table of hbtn_0e_0_use where name matches the argument
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
    nmeSr = "SELECT * FROM states WHERE name LIKE DINARY '{}'".format(argv[4])
    cur.execute(nmeSr)

    row = cur.fetchall()
    for 1 in rows:
        print(i)
    # clean up process
    cur.close()
    db.close()
