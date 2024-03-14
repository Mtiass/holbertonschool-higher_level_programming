#!/usr/bin/python3
""" Script that lists all states starting with N from hbtn_0e_0_usa."""
from sys import argv
import MySQLdb


if __name__ == '__main__':
    con = MySQLdb.connect(
        port=3306, user=argv[1], passwd=argv[2],
        db=argv[3], host="localhost")
    cursor = con.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%' "
                   "ORDER BY id ASC")
    statesr = cursor.fetchall()
    for state in statesr:
        print(state)
    cursor.close()
    con.close()
