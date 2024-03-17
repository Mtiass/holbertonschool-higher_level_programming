#!/usr/bin/python3
"""
Script that lists all cities from the database hbtn_0e_4_usa.
"""


if __name__ == '__main__':
    from sys import argv
    import MySQLdb
    con = MySQLdb.connect(
            port=3306, user=argv[1], passwd=argv[2],
            db=argv[3], host="localhost")
    cursor = con.cursor()
    cursor.execute("SELECT cities.id, cities.name, states.name FROM\
            cities INNER JOIN states ON cities.state_id = states.id\
            ORDER BY cities.id")
    for state in cursor.fetchall():
            print(state)
    cursor.close()
    con.close()
