import mysql.connector as msql
from mysql.connector import Error
from private.my_password import my_password

def connect_to_db(database):
    """Conecta a database"""
    try: 
        conn = msql.connect(host='localhost', database=database, user='root', password=my_password)
        if conn.is_connected():
            cursor = conn.cursor()
            cursor.execute("select database();")
            record = cursor.fetchone()
            print("Conectado a database: ", record)
            return cursor
    except Error as e:
        print("Error al conectar con MySQL", e)