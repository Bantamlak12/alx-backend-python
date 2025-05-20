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
        # Check if this query is inside of query_cache dict
        current_query = kwargs["query"]
        if len(query_cache) > 0:
            for cached_query in query_cache.values():
                # If query is cached, use the cached one
                if cached_query == current_query:
                    kwargs["query"] = cached_query
                    return func(*args, **kwargs)
                else:
                    # If the cache doesn't exist, create the cache
                    key = datetime.now()
                    query_cache[key] = current_query
        query_cache[datetime.now()] = current_query
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
