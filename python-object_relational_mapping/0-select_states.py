#!/usr/bin/python3
"""
Script that lists all states from the database hbtn_0e_0_usa.
"""
import sys
import MySQLdb

def main():

    con = MySQLdb.connect(
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        host='localhost',
        port=3306
        )

    cursor = con.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    states = cursor.fetchall()

    for state in states:
        print(state)

if __name__ == '__main__':
    main()
