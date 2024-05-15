#!/usr/bin/python3

from model_city import Base, City
from model_state import State
import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


def list_states(username, password, database):
    """this module queries the database."""

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(username, password, database),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(City, State).join(State).order_by(City.id).all()
    # loop running through the retrieved rows
    for city, state in states:
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    session.close()


if __name__ == "__main__":
    # main function
    if len(sys.argv) != 4:
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    list_states(username, password, database)
