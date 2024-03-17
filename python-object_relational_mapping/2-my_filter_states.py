#!/usr/bin/python3
"""
Script that takes in an argument and displays all values in the table of
hbtn_0e_0_usa where name matches the argument.
"""


if __name__ == '__main__':
    from sys import argv
    import MySQLdb
    con = MySQLdb.connect(
            port=3306, user=argv[1], passwd=argv[2],
            db=argv[3], host="localhost")
    cursor = con.cursor()
    cursor.execute("SELECT * FROM states WHERE name = '{}'\
            ORDER BY id ASC".format(argv[4]))
    for state in cursor.fetchall():    
            print(state)
    cursor.close()
    con.close()
