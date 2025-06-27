#!/usr/bin/python3
import MySQLdb
import sys
"""
that lists all states from the
database hbtn_0e_0_usa
"""


if __name__ == "__main__":	
    db_connection = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )
    cursor = db_connection.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id;")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db_connection.close()
