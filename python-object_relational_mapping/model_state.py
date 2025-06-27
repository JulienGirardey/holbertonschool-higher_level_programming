#!/usr/bin/python3
"""
6-model_state
that creates the State class
and the Base class
for the database hbtn_0e_6_usa
and creates the states table
in the database
using SQLAlchemy ORM
This module defines the State class, which represents a state in the database.
It inherits from Base and defines the table structure for states.
It includes columns for id and name.
It uses SQLAlchemy to define the database schema.
It is used in conjunction with the model_city module to create a relationship
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
class State(Base):
	"""State class that represents a state in the database."""
	__tablename__ = 'states'
	id = Column(Integer, primary_key=True)
	name = Column(String(128), nullable=False)
