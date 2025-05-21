import os
import mysql.connector
from dotenv import load_dotenv

load_dotenv()

# Database credentials
database = os.environ.get("DATABASE_NAME")
user = os.environ.get("USER")
password = os.environ.get("PASSWORD")
host = os.environ.get("HOST")

class DatabaseConnection:
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
            print(f"Database connection failed. {err}")
            raise
        finally:
            return self.cursor

    def __exit__(self, exc_type, exc_value, traceback):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()
        if exc_type:
            return False

def main():
    try:
        with DatabaseConnection(database, user, password, host) as cursor:
            cursor.execute("SELECT * FROM users")
            results = cursor.fetchall()
            print(results)
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()

