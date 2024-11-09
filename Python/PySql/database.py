import mysql.connector
from mysql.connector import Error


def database_connection():
        conn = mysql.connector.connect(
                # Because we can not.
        )
        return conn
