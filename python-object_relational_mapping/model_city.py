#!/usr/bin/python3
"""
This module defines the City class which links to the MySQL table cities
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
