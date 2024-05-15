#!/usr/bin/python3
"""this module defines a funtion that issue a query to the database"""

import sys
import MySQLdb


def list_cities(username, password, database):
    """this function issue a query to the database"""

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )
    cursor = db.cursor()
    cursor.execute("SELECT cities.id, cities.name, states.name\
                    FROM cities JOIN states WHERE cities.state_id\
                    = states.id ORDER BY cities.id ASC")

    cities = cursor.fetchall()
    for city in cities:
        city_id, state_name, city_name = city
        print("({}, '{}', '{}')".format(city_id, state_name, city_name))

    cursor.close()
    db.close()


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    list_cities(username, password, database)
