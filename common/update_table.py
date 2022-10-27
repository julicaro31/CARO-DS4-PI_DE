import mysql.connector as msql
from mysql.connector import Error
from private.my_password import my_password #contraseña de MySQL
import pandas as pd

def update_table(nombre_bd,nombre_tabla):
    
    """ 
        Se actualiza la tabla de precios de los productos.
    """
    
    try: 
        conn = msql.connect(host='localhost', database=nombre_bd, user='root', password=my_password)
        if conn.is_connected():
            cursor = conn.cursor()
            cursor.execute("select database();")
            record = cursor.fetchone()
            print("Conectado a database: ", record)

            ## Se actualizan los precios de la nueva semana
            print("Actualizando precios...")
            sql_1 = f'UPDATE precio INNER JOIN {nombre_tabla} ON (precio.IdProducto = {nombre_tabla}.IdProducto AND precio.IdSucursal = {nombre_tabla}.IdSucursal) SET precio.Precio = {nombre_tabla}.Precio;;'
            cursor.execute(sql_1)
            ## Se insertan los productos nuevos (que antes no se encontaban en la tabla precio)
            print("Insertando nuevos productos...")
            sql_2 = f'INSERT into precio SELECT {nombre_tabla}.IdProducto,{nombre_tabla}.IdSucursal,{nombre_tabla}.Precio FROM {nombre_tabla} LEFT JOIN precio ON (precio.IdProducto = {nombre_tabla}.IdProducto AND precio.IdSucursal = {nombre_tabla}.IdSucursal) WHERE (precio.IdProducto IS NULL AND precio.IdSucursal IS NULL);'
            cursor.execute(sql_2)
            conn.commit()
    except Error as e:
        print("Error al conectar con MySQL", e)