import sqlite3
import functools
from datetime import datetime

#### decorator to lof SQL queries

def log_queries(func):
    """Decorator to log SQL queries"""
    # @functools.wraps(func) # Helps the function to retail its original identity
    def wrapper(*args, **kwargs):
        query = kwargs.get('query')
        print(f"{datetime.now().strftime("%Y-%m-%d %H:%S,%f")[:-3]} {query}")
        return func(*args, **kwargs)
    return wrapper

@log_queries
def fetch_all_users(query):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results

#### fetch users while logging the query
users = fetch_all_users(query="SELECT * FROM users")
