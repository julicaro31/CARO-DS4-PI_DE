from datetime import datetime
import os
from common.paths import path_data_clean

def transform_semanal(df,csv_nombre:str):
    """ 
        Transforma dataframe extraído de archivo 'precios_semana_*_' y lo guarda en un nuevo csv.
    """

    df.precio = df.precio.apply(lambda x: None if x == "" else x )
    
    df.producto_id = df.producto_id.astype(str).apply(lambda x: x.split('-')[-1].zfill(13))

    df.sucursal_id = df.sucursal_id.apply(lambda x: str(x.day) + '-' + str(x.month) + '-' + str(x.year) if type(x)==datetime else x)

    df = df[df.precio < 100000] #outliers
    
    df.drop_duplicates(subset=['producto_id','sucursal_id'],keep="last",inplace=True)

    df.dropna(inplace=True)

    df.to_csv(os.path.join(path_data_clean,csv_nombre),columns = ['producto_id','sucursal_id','precio'] ,header=['IdProducto','IdScursal','Precio'],index=False)


def transform_producto(df,csv_nombre:str):
    """
        Transforma dataframe extraído de archivo 'producto' y lo guarda en un nuevo csv.
    """
    
    df.id = df.id.astype(str).apply(lambda x: x.split('-')[-1].zfill(13))

    df.nombre = df.nombre.astype(str).apply(lambda x: x.title())

    df.marca = df.marca.astype(str).apply(lambda x: x.title())

    df.drop(['categoria1','categoria2','categoria3'],axis=1,inplace=True)

    df.fillna('Sin Dato',inplace=True)

    df.drop_duplicates(subset='id',keep="last",inplace=True)

    df.to_csv(os.path.join(path_data_clean,csv_nombre),header=['IdProducto','Marca','Nombre','Presentacion'],index=False)
    


def transform_sucursal(df,csv_nombre:str):

    """
        Transforma dataframe extraído de archivo 'sucursal' y lo guarda en un nuevo csv.
    """

    columns = ['banderaDescripcion','comercioRazonSocial','localidad', 'direccion','sucursalNombre', 'sucursalTipo']

    for column in columns:
        df[column] = df[column].astype(str).apply(lambda x: x.title())

    df.provincia = df.provincia.astype(str).apply(lambda x: x.upper())
    
    df.fillna('Sin Dato',inplace=True)

    df.drop_duplicates(subset='id',keep="last",inplace=True)

    df.to_csv(os.path.join(path_data_clean,csv_nombre),header=['IdSucursal','ComercioId','BanderaId','BanderaDescripcion','ComercioRazonSocial','Provincia','Localidad','Direccion','Lat','Lng','SucursalNombre','SucursalTipo'],index=False)


