#!/usr/bin/python3
"""Lists all cities from the database hbtn_0e_4_usa"""
import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    connection = MySQLdb.connect(host="localhost", user=username,
                                 password=password, db=database, port=3306)
    cursor = connection.cursor()

    cursor.execute("""SELECT cities.name
                   FROM cities
                   INNER JOIN states ON states.id=cities.state_id
                   WHERE states.name=%s""", (sys.argv[4],))
    cities = cursor.fetchall()

    print(", ".join(city[0] for city in cities))

    cursor.close()
    connection.close()
