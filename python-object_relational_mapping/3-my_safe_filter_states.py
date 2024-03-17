#!/usr/bin/python3
"""
Script that takes in arguments and displays all values in the states table
of hbtn_0e_0_usa where name matches the argument.
"""


if __name__ == '__main__':
    from sys import argv
    import MySQLdb
    con = MySQLdb.connect(
            port=3306, user=argv[1], passwd=argv[2],
            db=argv[3], host="localhost")
    cursor = con.cursor()
    cursor.execute("SELECT * FROM states WHERE name = %s\
            ORDER BY id ASC", (argv[4],))
    for state in cursor.fetchall():
        if state[1] == argv[4]:
            print(state)
    cursor.close()
    con.close()
