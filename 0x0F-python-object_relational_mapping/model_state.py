#!/usr/bin/python3
"""
model_state.py: contains class definition of a State
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

BaSe = declarative_base()


class State(BaSe):
    """
    maps to 'states' table in hbtn_0e_6_usa' database
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)

    def __repr__(self):
        return '<State(id={}, name={})>'.format(self.id, self.name)
