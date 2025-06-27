#!/usr/bin/python3
"""
14-model_city_fetch_by_state
that lists all City objects
from the database hbtn_0e_14_usa
and is ordered by cities.id (ascending)
The script should take 3 arguments: mysql username, mysql password and database name
It uses SQLAlchemy to connect to the MySQL database and fetches City objects along with their
associated State objects. It prints each city with its state name in the format:
"<state name>: (<city id>) <city name>"
If there are no cities, it will not print anything.
"""
from model_state import State, Base
from model_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
import sys


if __name__ == "__main__":
	engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
	Base.metadata.create_all(engine)
	Session = sessionmaker(bind=engine)
	session = Session()
	states = session.query(City, State).join(State, City.state_id == State.id).order_by(City.id)
	for city, state in states:
		print("{}: ({}) {}".format(state.name, city.id, city.name))
	session.close()
