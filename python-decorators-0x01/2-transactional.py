import sqlite3
import functools

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

def transactional(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        conn = kwargs.get("conn")
        if conn is None:
            raise ValueError("Database connection not found.")

        try:
            result = func(*args, **kwargs)
            conn.commit()
            return result
        except Exception as err:
            conn.rollback()
            raise
    return wrapper

@with_db_connection
@transactional 
def update_user_email(conn, user_id, new_email): 
    cursor = conn.cursor() 
    cursor.execute("UPDATE users SET email = ? WHERE id = ?", (new_email, user_id)) 


# Update user's email with automatic transaction handling 
update_user_email(user_id=1, new_email='Crawford_Cartwright@hotmail.com')
