import mysql.connector as msql
from mysql.connector import Error
from private.my_password import my_password #contraseña de MySQL
import pandas as pd

def add_fk(columna,nombre_bd,nombre_tabla,tabla_padre):
    """ 
        Agrega foreing keys.
    """
    
    try: 
        conn = msql.connect(host='localhost', database=nombre_bd, user='root', password=my_password)
        if conn.is_connected():
            cursor = conn.cursor()
            cursor.execute("select database();")
            record = cursor.fetchone()
            print("Conectado a database: ", record)
        
        cursor.execute('SET FOREIGN_KEY_CHECKS=0;')

        sql = f'ALTER TABLE {nombre_tabla} ADD CONSTRAINT foreign_{columna} FOREIGN KEY ({columna}) REFERENCES {tabla_padre}({columna});'
        print(sql)
        cursor.execute(sql)

        cursor.execute('SET FOREIGN_KEY_CHECKS=1;')
            
        conn.commit()
    except Error as e:
        print("Error al conectar con MySQL", e)