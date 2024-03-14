#!/usr/bin/python3
""" Script that lists all states from the database hbtn_0e_0_usa."""

if __name__ == '__main__':
    import sys
    import MySQLdb

    con = MySQLdb.connect(host='localhost', port=3306, user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3], charset='utf8')
    cursor = con.cursor()
    cursor.execute("SELECT * FROM states")
    statesr = cursor.fetchall()
    for state in statesr:
        print(state)
    cursor.close()
    con.close()
