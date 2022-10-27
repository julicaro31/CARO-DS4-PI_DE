import mysql.connector as msql
from mysql.connector import Error
from private.my_password import my_password #contraseña de MySQL

def create_table(nombre_bd:str,nombre_tabla:str,variables:str):
    """
        Crea tabla de una base de datos. De existir se elimina.
        Variables especifica las columnas de las tablas y su tipo de dato.
        Debe escribirse en formato del lenguaje MySQL.
    """
    query_1 = f'DROP TABLE IF EXISTS {nombre_tabla};'
    query_2 = f"CREATE TABLE {nombre_tabla}({variables})ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;"
    try: 
        conn = msql.connect(host='localhost', database=nombre_bd, user='root', password=my_password)
        if conn.is_connected():
            cursor = conn.cursor()
            cursor.execute("select database();")
            record = cursor.fetchone()
            print("Conectado a database: ", record)
            #Creo tablas
            cursor.execute(query_1)
            print('Creando tabla....')
            cursor.execute(query_2)
            print("La tabla ha sido creada")
    except Error as e:
        print("Error al conectar con MySQL", e)