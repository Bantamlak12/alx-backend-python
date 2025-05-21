import os
import asyncio
import aiosqlite
import mysql.connector
from dotenv import load_dotenv

load_dotenv()

# Database credentials
database = os.environ.get("DATABASE_NAME")

class AsyncDatabaseConnection:
    """Custom class based context manager for database connection"""
    def __init__(self, database):
        self.database = database
        self.connection = None
        self.cursor = None

    async def __aenter__(self):
        try:
            self.connection = await aiosqlite.connect(self.database)
            self.cursor = await self.connection.cursor()
            return self.cursor
        except Exception as err:
            print(f"Database connection failed. {err}")
            raise

    async def __aexit__(self, exc_type, exc_value, traceback):
        if self.cursor:
            await self.cursor.close()
        if self.connection:
            await self.connection.close()
        if exc_type:
            return False


class AsyncExecuteQuery(AsyncDatabaseConnection):

    def __init__(self, base_query, column, operator, value, database=database):
        super().__init__(database)

        self.base_query = base_query
        self.column = column
        self.operator = operator
        self.value = value

    async def __aenter__(self):
        cursor = await super().__aenter__()
        try:
            sql_query = f"{self.base_query} WHERE {self.column} {self.operator} ?"
            await cursor.execute(sql_query, (self.value,))
            return await cursor.fetchall()
        except Exception as e:
            print(f"Error while Executing the query. {e}")
            raise

    async def __aexit__(self, exc_type, exc_value, traceback):
        return await super().__aexit__(exc_type, exc_value, traceback)

async def async_fetch_users():
    base_query = "SELECT * FROM users"
    async with AsyncExecuteQuery(base_query, "age", ">", 0) as users:
        return users

async def async_fetch_older_users():
    base_query = "SELECT * FROM users"
    async with AsyncExecuteQuery(base_query, "age", ">", 40) as older_users:
        return older_users

async def fetch_concurrently():
    batch = await asyncio.gather(async_fetch_users(), async_fetch_older_users())
    users, older_users = await batch
    
    print(f"Users:\n {users}\n")
    print(f"Older users: \n{older_users}")

if __name__ == "__main__":
    asyncio.run(fetch_concurrently())



