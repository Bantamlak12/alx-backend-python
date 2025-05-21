import mysql.connector
from datetime import datetime

class DatabaseConnection():
    """Custom class based context manager for database connection"""
    def __init__(self, database, user, password, host="localhost"):
        self.database = database
        self.host = host
        self.user = user
        self.password = password
        self.connection = None
        self.cursor = None

    def __enter__(self):
        try:
            connection = mysql.connector.connect(
                host = self.host,
                user = self.user,
                password = self.password,
                database = self.database
            )
            self.connection = connection
            self.cursor = connection.cursor()
        except Exception as err:
            print("Database connection failed. Double check database name or credentials you passed.")
        finally:
            return self.cursor

    def __exit__(self, exc_type, exc_value, traceback):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()
        if exc_type:
            return False


with DatabaseConnection("ALX_prodev", "bantamlak", "dispensed") as cursor:
    cursor.execute("SELECT * FROM users")
    results = cursor.fetchall()
    print(results)

