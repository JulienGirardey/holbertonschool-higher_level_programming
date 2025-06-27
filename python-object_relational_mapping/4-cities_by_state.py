#!/usr/bin/python3
"""
4-cities_by_state
that lists all cities from the database hbtn_0e_4_usa
and is ordered by cities.id (ascending)
This script connects to a MySQL database using the credentials provided as command line arguments.
It retrieves all cities along with their corresponding state names, ordered by city id.
Usage: ./4-cities_by_state.py <mysql username> <mysql password> <database name>
"""
import MySQLdb
import sys


if __name__ == "__main__":
	db = MySQLdb.connect(
		host="localhost",
		port=3306,
		user=sys.argv[1],
		passwd=sys.argv[2],
		db=sys.argv[3]
	)
	cursor = db.cursor()
	query = "SELECT cities.id, cities.name, states.name FROM cities INNER JOIN states ON cities.state_id = states.id ORDER BY cities.id;"
	cursor.execute(query)
	rows = cursor.fetchall()
	for row in rows:
		print(row)
	cursor.close()
	db.close()
