#!/usr/bin/python3
"""this module defines a class that will be
connected to a database via orm"""

from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base

# creating the base class for the connection
Base = declarative_base()


class State(Base):
    """the class repr of the table 'states' in the database"""
    # the name of the table representing the class in the database
    __tablename__ = 'states'

    id = Column(Integer, nullable=False, autoincrement=True, primary_key=True)
    name = Column(String(128), nullable=False)
