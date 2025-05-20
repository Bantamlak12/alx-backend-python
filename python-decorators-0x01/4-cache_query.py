import time
import sqlite3
import functools
from datetime import datetime

query_cache = {}

# A decorator that creates a database connection
def with_db_connection(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        conn = sqlite3.connect("users.db")
        try:
            kwargs["conn"] = conn # For down stream use
            return func(*args, **kwargs)
        finally:
            conn.close()
    return wrapper

# A decorator that caches queries
def cache_query(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        query = kwargs.get("query")
        if query in query_cache:
            print(f"Using cached query result, and it is {query_cache[query]}")
            return query_cache[query]
        print("Query result was not cached")
        # Run the query and cache the result
        result = func(*args, **kwargs)
        query_cache[query] = result
        return result
    return wrapper

@with_db_connection
@cache_query
def fetch_users_with_cache(conn, query):
    cursor = conn.cursor()
    cursor.execute(query)
    return cursor.fetchall()

# First call will cache the result
users = fetch_users_with_cache(query="SELECT * FROM users")

# Second call will use the cached result
users_again = fetch_users_with_cache(query="SELECT * FROM users")
