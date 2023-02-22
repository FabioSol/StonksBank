import pandas as pd
import pyodbc
from pyodbc import Row
import random
import string


def db_connection_cursor(func):
    def wrapper(self, *args, **kwargs):
        # Open connection to database
        conn = pyodbc.connect(self.conn_str)
        cursor = conn.cursor()
        try:
            # Call the function with the database connection
            result = func(self, cursor, *args, **kwargs)
            return result
        finally:
            # Close the database connection
            cursor.close()
            conn.close()

    return wrapper



class Editor:
    def __init__(self,
                 server: str = "tcp:stonksbankserver.database.windows.net",
                 port: str = "1433",
                 database: str = "StonksBankDB",
                 username: str = "Stonk",
                 password: str = "Demoac123",
                 driver: str = "SQL Server"):

        self.server = server
        self.port = port
        self.database = database
        self.username = username
        self.password = password
        self.driver = driver

        # Create the connection string
        self.conn_str = f"Driver={driver};Server={server},{port};Database={database};Uid={username};Pwd={password};" \
                        f"Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;"

        conn = pyodbc.connect(self.conn_str)
        cursor = conn.cursor()
        query = "SELECT SCHEMA_NAME()"
        cursor.execute(query)
        self.schema = cursor.fetchone()[0]
        cursor.close()
        conn.close()
        self.default_schema = self.schema

    def test_connection(self) -> bool:
        # Try to connect to the database
        try:
            conn = pyodbc.connect(self.conn_str)
            conn.close()
            return True
        except pyodbc.Error as ex:
            raise Exception(f'Connection failed: {ex}')


