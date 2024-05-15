#!/usr/bin/python3
"""this module queries the database"""

from model_state import Base, State
import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


def list_states(username, password, database):
    """this module queries the database"""

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(username, password, database),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).filter(State.name.like('%a%')).\
        order_by(State.id).all()

    for state in states:
        print(state)

    session.close()


if __name__ == "__main__":
    if len(sys.argv) != 4:
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    list_states(username, password, database)
