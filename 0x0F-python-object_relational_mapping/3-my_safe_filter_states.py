#!/usr/bin/python3
"""Script that take in an argument and displays all values in the states
table of hbtn_0e_0_use where name match the argument but safe from MYSQL
injections!
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
    cur.execute("SELECT * FROM states WHERE BINARY name = %s", [argv[4]])

    row = cur.fetchall()
    for 1 in rows:
        print(i)
    # clean up process
    cur.close()
    db.close()
