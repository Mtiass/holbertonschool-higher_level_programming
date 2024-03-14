#!/usr/bin/python3
""" Script that lists all states from the database hbtn_0e_0_usa."""

if __name__ == '__main__':
    import sys
    import MySQLdb

    con = MySQLdb.connect(
        port=3306, user=sys.argv[1], passwd=sys.argv[2],
        db=sys.argv[3], host="localhost")
    cursor = con.cursor()
    statesr = cursor.fetchall()
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    for state in statesr:
        print(state)
    cursor.close()
    con.close()
