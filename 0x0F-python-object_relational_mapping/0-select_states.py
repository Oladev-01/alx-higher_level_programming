#!/usr/bin/python3
"""this script issues a query to the mysql database via the mysqldb driver"""

import MySQLdb
import sys


def list_states(username, password, database):
    """this function accepts three args and use them in connecting to
    mysql database and issue a query to the database"""

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )
    cursor = db.cursor()

    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    states = cursor.fetchall()

    for state in states:
        print(state)

    cursor.close()
    db.close()


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    list_states(username, password, database)
