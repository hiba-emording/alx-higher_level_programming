#!/usr/bin/python3
"""Lists all states from the database hbtn_0e_0_usa"""
import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    connection = MySQLdb.connect(host="localhost", user=username,
                                 password=password, db=database, port=3306)
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM states WHERE name LIKE BINARY '{}'"
                   .format(sys.argv[4]))
    states = cursor.fetchall()

    for state in states:
        print(state)

    cursor.close()
    connection.close()
