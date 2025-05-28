import mysql.connector
from dotenv import load_dotenv
import os

# ensure the .env file is in the same directory as this script
dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if not os.path.exists(dotenv_path):
    print(f"Error: .env file not found at {dotenv_path}")
else:
    print(f"Loading .env from {dotenv_path}")

load_dotenv(dotenv_path)

print("MYSQL_HOST:", os.getenv('MYSQL_HOST'))  # Debug

def get_db_connection():
    """Establish a connection to the MySQL database."""
    load_dotenv()
    try:
        connection = mysql.connector.connect(
            host=os.getenv('MYSQL_HOST'),
            user=os.getenv('MYSQL_USER'),
            password=os.getenv('MYSQL_PASSWORD'),
            database=os.getenv('MYSQL_DATABASE')
        )
        print("Database connection established.")
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