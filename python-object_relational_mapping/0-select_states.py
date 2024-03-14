#!/usr/bin/python3
# Script that lists all states from the database hbtn_0e_0_usa.
import sys
import MySQLdb


if __name__ == '__main__':

    con = MySQLdb.connect(
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        host='localhost',
        port=3306
        )

    cursor = con.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
