import psycopg2

DB_NAME = "contracts"

def get_database_connection():
    """
    this function should create a connection
    to the database and return the connection
    """

    conn = psycopg2.connect(dbname=DB_NAME, user="cloud_user")
    return conn

