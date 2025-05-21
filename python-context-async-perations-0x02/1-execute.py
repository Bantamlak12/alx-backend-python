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


class ExecuteQuery(DatabaseConnection):

    def __init__(self, base_query, column, operator, value, database=database, user=user, password=password, host=host):
        super().__init__(database, user, password, host)

        self.base_query = base_query
        self.column = column
        self.operator = operator
        self.value = value

    def __enter__(self):
        cursor = super().__enter__()
        try:
            sql_query = f"{self.base_query} WHERE {self.column} {self.operator} ?"
            cursor.execute(sql_query, (self.value,))
            return cursor.fetchall()
        except Exception as e:
            print(f"Error while Executing the query. {e}")
            raise

    def __exit__(self, exc_type, exc_value, traceback):
        return super().__exit__(exc_type, exc_value, traceback)

def main():
    query = "SELECT * FROM users"
    column = "age"
    age = 25
    operator = ">"
    with ExecuteQuery(base_query=query, column=column, operator=operator, value=age) as results:
        print(results)

if __name__ == "__main__":
    main()

