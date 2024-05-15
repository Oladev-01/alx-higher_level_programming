#!/usr/bin/python3
"""this module defines a function that issue a query to the database"""

import sys
import MySQLdb


def list_cities(username, password, database, state_type):
    """this function issue a query to the database"""

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )
    cursor = db.cursor()
    query = "SELECT cities.name from states JOIN cities\
          ON states.id = cities.state_id WHERE states.name = %s"
    cursor.execute(query, (state_type,))

    cities = cursor.fetchall()
    city_name = []
    for city in cities:
        city_name.append(city[0])
    print(", ".join(city_name))

    cursor.close()
    db.close()


if __name__ == "__main__":
    if len(sys.argv) != 5:
        sys.exit(1)
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    list_cities(username, password, database, state_name)
