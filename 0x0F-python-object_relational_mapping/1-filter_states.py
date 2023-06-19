#!/usr/bin/python3

import sys
import MySQLdb

if __name__ == "__main__":
    mysql_user = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    db_connect = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_user,
        passwd=mysql_password,
        db=database_name
    )

    cursor = db_connect.cursor()

    query = "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC"

    cursor.execute(query)

    rows = cursor.fetchall()

    for row in rows:
        print(row)
