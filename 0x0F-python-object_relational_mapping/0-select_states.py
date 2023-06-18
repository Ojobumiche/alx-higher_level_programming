#!/usr/bin/python3
import MySQLdb

def list_state(user_name, password, database):
    db = MySQLdb.connect(host='localhost', port=3306, user='user_name', 
            password='password', db='database');
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC");
    state = cursor.fetchall();
    for state in states:
        print(state)
    
    cursor.close()
    db.close()

    if __name__ == '__main__':
        import sys
        if len(sys.argv) < 4:
            print("Usage: python list_states.py <user_name> <password> <database>")
        else: 
            user_name = sys.argv[1]
            password  = sys.argv[2]
            database = sys.argv[3]
            list_states(user_name, password, database)

