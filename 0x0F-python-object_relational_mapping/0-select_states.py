#!/usr/bin/python3
"""
Retrieves and lists all states from the 'hbtn_0e_0_usa' database.
"""
import MySQLdb
import sys

def list_states(username, password, database):
    """
    Connects to the MySQL database and lists all states.
    """
    try:
        # Establishing the connection to the database
        connection = MySQLdb.connect(
            host="localhost",
            user=username,
            passwd=password,
            db=database,
            port=3306
        )

        # Creating a cursor object to interact with the database
        with connection.cursor() as cursor:
            # Defining and executing the SQL query
            cursor.execute("SELECT * FROM states")
            
            # Fetching and printing each row from the result set
            for state in cursor.fetchall():
                print(state)
    
    except MySQLdb.Error as e:
        print(f"Error {e}")
    
    finally:
        # Ensuring the connection is closed after the operation
        if connection:
            connection.close()

if __name__ == "__main__":
    if len(sys.argv) == 4:
        list_states(sys.argv[1], sys.argv[2], sys.argv[3])
    else:
        print("Usage: ./script.py <username> <password> <database>")

