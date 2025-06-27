#!/usr/bin/python3
"""
6-model_city
that creates the City class
and the Base class
for the database hbtn_0e_6_usa
and creates the cities table
in the database
using SQLAlchemy ORM
This module defines the City class, which represents a city in the database.
It inherits from Base and defines the table structure for cities.
It includes columns for id, state_id, and name.
It uses SQLAlchemy to define the database schema.
It is used in conjunction with the model_state module to create a relationship
between cities and states.
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy import ForeignKey
from model_state import Base


class City(Base):
	"""City class that represents a city in the database."""
	__tablename__ = 'cities'
	id = Column(Integer, primary_key=True)
	state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
	name = Column(String(128), nullable=False)
