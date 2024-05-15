#!/usr/bin/python3
"""this module queries the database"""

from model_state import Base, State
import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


def list_states(username, password, database, query_type):
    """this module queries the database"""

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(username, password, database),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).filter(State.name.like
                                         ('%{}%'.format(query_type))).all()

    if not states:
        print("Not found")
        return
    try:
        for state in states:
            print(state.id)
    except Exception as e:
        print("this is what went wrong: {}".format(e))

    session.close()


if __name__ == "__main__":
    if len(sys.argv) != 5:
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    query_type = sys.argv[4]

    list_states(username, password, database, query_type)
