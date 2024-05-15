#!/usr/bin/python3
"""this module defines a function isues a query to the
database via user input"""

import sys
import MySQLdb


def list_states(username, password, database, query_type):
    """this function isues a query to the database via user input"""
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )
    cursor = db.cursor()
    query = "SELECT * FROM states WHERE BINARY name LIKE\
          '{}'".format(query_type)
    cursor.execute(query)
    states = cursor.fetchall()
    for state in states:
        print(state)

    cursor.close()
    db.close()


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    query_type = sys.argv[4]
    list_states(username, password, database, query_type)
