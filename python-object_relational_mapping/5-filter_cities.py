#!/usr/bin/python3
"""
Script that takes in the name of a state as an argument and lists all
cities of that state, using the database hbtn_0e_4_usa.
"""


if __name__ == '__main__':
    from sys import argv
    import MySQLdb
    con = MySQLdb.connect(
            port=3306, user=argv[1], passwd=argv[2],
            db=argv[3], host="localhost")
    cursor = con.cursor()
    cursor.execute("SELECT cities.name FROM cities INNER JOIN states ON\
            cities.state_id = states.id WHERE states.name = %s ORDER BY\
            cities.id", (argv[4],))
    li = []
    for cities in cursor.fetchall():
        for n in cities:
            li.append(n)
    print(", ".join(li))
    cursor.close()
    con.close()
