#!/usr/bin/python3
""" Script that lists all states from the database hbtn_0e_0_usa."""
from sys import argv
import MySQLdb


if __name__ == '__main__':

    if len(argv) < 4:
        print("Usage: {} username password database_name".format(argv[0]))
        exit(1)
    con = MySQLdb.connect(
        port=3306, user=argv[1], passwd=argv[2],
        db=argv[3], host="localhost")
    cursor = con.cursor()
    cursor.execute("SELECT * FROM states ORDER BY states.id ASC")
    statesr = cursor.fetchall()
    for state in statesr:
        print(state)
    cursor.close()
    con.close()
