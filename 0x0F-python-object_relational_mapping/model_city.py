#!/usr/bin/python3



from sqlalchemy import Column, String, Integer, ForeignKey, create_engine
from model_state import Base


class City(Base):
    """this class defines class repr of the cities table"""
    __tablename__ = 'cities'

    id = Column(Integer, nullable=False, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)

    engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format
                           ('root', '1002', 'localhost', 'hbtn_0e_14_usa'))
    Base.metadata.create_all(engine)
