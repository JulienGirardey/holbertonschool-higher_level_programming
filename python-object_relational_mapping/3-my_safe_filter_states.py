#!/usr/bin/python3
"""
1-filter_states
that lists all states from the
database hbtn_0e_0_usa
where name starts with 'n'
and is ordered by id (ascending)
This script uses parameterized queries to prevent SQL injection.
It connects to a MySQL database using the credentials
provided as command line arguments.
It retrieves all states whose names start with 'n' and orders them by id.
It prints each state as a tuple (id, name).
Usage: ./3-my_safe_filter_states.py <mysql username>
<mysql password> <database name> <state name>
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
    name_search = sys.argv[4]
    cursor = db.cursor()
    query = "SELECT * FROM states WHERE name = %s ORDER BY id;"
    cursor.execute(query, (name_search,))
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()
