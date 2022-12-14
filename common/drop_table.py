import mysql.connector as msql
from mysql.connector import Error
from private.my_password import my_password #contraseña de MySQL
import pandas as pd

def drop_table(nombre_bd,nombre_tabla):
    
    """ 
        Elimina la tabla 'nombre_tabla' de la base de datos 'nombre_bd'
    """
    
    try: 
        conn = msql.connect(host='localhost', database=nombre_bd, user='root', password=my_password)
        if conn.is_connected():
            cursor = conn.cursor()
            cursor.execute("select database();")
            record = cursor.fetchone()
            print("Conectado a database: ", record)

            sql = f"DROP TABLE {nombre_tabla}"
            cursor.execute(sql)
            conn.commit()
            print(f"La tabla {nombre_tabla} ha sido eliminada")
    except Error as e:
        print("Error al conectar con MySQL", e)