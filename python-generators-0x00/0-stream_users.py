import mysql.connector
import mysql.connector.errorcode

def stream_users():
    connection = mysql.connector.connect(
        host="localhost",
        user="bantamlak",
        password="dispensed",
        database="ALX_prodev"
    )
    cursor = connection.cursor()
    try:
        cursor.execute("SELECT * FROM user_data")
    except mysql.connector.Error as err:
        print("Error while fetching user data. {}".format(err))

    while True:
        row = cursor.fetchone()
        if row is None:
            break
        yield row

    cursor.close()
    connection.close()
