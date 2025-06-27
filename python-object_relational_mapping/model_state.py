#!/usr/bin/python3
"""
This module defines the State class and the Base class for use with SQLAlchemy ORM.
It creates the 'states' table in the database hbtn_0e_6_usa and is used in conjunction
with model_city to create relationships between states and cities.
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
class State(Base):
	"""State class that represents a state in the database."""
	__tablename__ = 'states'
	id = Column(Integer, primary_key=True)
	name = Column(String(128), nullable=False)
