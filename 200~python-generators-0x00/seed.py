import csv
import mysql.connector
import mysql.connector.errorcode

def connect_db():
    """ Connects to MySQL server.

    Returns:
            MySQL connection
    """
    return mysql.connector.connect(
        host="localhost",
        user="bantamlak",
        password="dispensed"
    )

def create_database(connection):
    """"Creates the ALX_prodev database if it doesn't exist."""
    cursor = connection.cursor()
    try:
        cursor.execute("CREATE DATABASE IF NOT EXISTS ALX_prodev")
    except mysql.connector.Error as err:
        print("Error while creating a database: {}".format(err))
    finally:
        cursor.close()

def connect_to_prodev():
    """Connects to the ALX_prodev database.

    Returns:
        Connection to the ALX_prodev database
    """
    return mysql.connector.connect(
        host="localhost",
        user="bantamlak",
        password="dispensed",
        database="ALX_prodev"
    )

def create_table(connection):
    """Creates user_data table if it doesn't exist."""
    cursor = connection.cursor()
    user_table_query = """
    CREATE TABLE IF NOT EXISTS user_data (
        user_id VARCHAR(36) PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        email VARCHAR(255) NOT NULL,
        age DECIMAL NOT NULL,
        
        INDEX (email)
    )
    """
    try:
        cursor.execute(user_table_query)
    except mysql.connector.Error as err:
        print("Error while creating a table: {}".format(err))
    finally:
        cursor.close()

def read_csv_generator(file_path):
    """Yields rows from the csv file"""
    with open(file_path, 'r', newline='', encoding='utf-8') as file:
        csv_reader = csv.reader(file)
        # Skip the header as it contains the unnecessary data for the db
        next(csv_reader)
        for row in csv_reader:
            yield row

def insert_data(connection, file_path):
    """Migrates data from the generated row to user_data table if email is not duplicated."""
    cursor = connection.cursor()

    generator_row = read_csv_generator(file_path)
    for row in generator_row:
        name, email, age = row[0], row[1], row[2]

        try:
            # Check if the email is already exist in the table
            cursor.execute("SELECT email FROM user_data WHERE email = %s", (email,))

            # Skip if there is duplicated row
            if cursor.fetchone():
                continue

            cursor.execute("INSERT INTO user_data (user_id, name, email, age) VALUES (UUID(), %s, %s, %s)", (name, email, age))
        except mysql.connector.Error as err:
            print("Error while inserting data: {}".format(err))

    # Save and close
    connection.commit()
    cursor.close()
