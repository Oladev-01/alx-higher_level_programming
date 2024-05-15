#!/usr/bin/python3
"""this module queries the database"""

from relationship_state import Base, State
from relationship_city import City
import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


def list_states(username, password, database):
    """this module queries the database"""

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(username, password, database),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    new_state = State(name="California")
    new_city = City(name="San Francisco", state=new_state)
    session.add(new_state)
    session.add(new_city)

    session.commit()

    session.close()


if __name__ == "__main__":
    if len(sys.argv) != 4:
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    list_states(username, password, database)
