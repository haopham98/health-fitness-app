import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()


def get_db_connection():
    """Establish a connection to the MySQL database."""
    try:
        connection = mysql.connector.connect(
            host=os.getenv('MYSQL_HOST'),
            user=os.getenv('MYSQL_USER'),
            password=os.getenv('MYSQL_PASSWORD'),
            database=os.getenv('MYSQL_DATABASE')
        )
        return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None


def execute_query(connection, query, params=None):
    """Execute a query on the database."""
    if connection is None:
        print("No database connection established.")
        return None
    # Use buffered=True to fetch results later
    cursor = connection.cursor(buffered=True)
    try:
        cursor.execute(query, params)
        connection.commit()
        return cursor.fetchall()
    except mysql.connector.Error as err:
        print(f"Error executing query: {err}")
        return None
    finally:
        cursor.close()


def close_db_connection(connection):
    """Close the database connection."""
    if connection:
        try:
            connection.close()
            print("Database connection closed.")
        except mysql.connector.Error as err:
            print(f"Error closing connection: {err}")
    else:
        print("No connection to close.")


if __name__ == "__main__":
    # Example usage
    conn = get_db_connection()
    if conn:
        result = execute_query(conn, "SELECT * FROM Foods;")
        print(result)
        close_db_connection(conn)
    else:
        print("Failed to connect to the database.")