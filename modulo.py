# -*- coding: utf-8 -*-
"""
Created on Tue Aug 30 10:18:55 2022

@author: YENIFER
"""

import pandas as pd
import numpy as np

def cargaDatos(ruta, fichero, separador=','):
    datos=pd.read_csv(ruta+fichero, sep= separador)
    return datos

def dameColumnas(datos):
    return datos.columns

def cambiaColumnas(datos, columnas):
    datos.columns = columnas
    return datos

def guardarDatos(datos,ruta, fichero):
    datos.to_csv(ruta+fichero)
    return True

def dameEstadisticos(datos,tipo='numerico'):
    """tipo numerico o todos """
    if tipo=='numerico':
        return datos.describe()
    else:
        return datos.describe(include = 'all')
                

def reemplazarNulos(datos, columna):
    media = datos[columna].mean()
    datos[columna].replace(np.nan, media, inplace= True)
    return datos

def cambiarTipo(columna, tipo='float64'):
    #columna = columna.astype(tipo)
    #datos['potencia']=pd.to_numeric(datos['pontencia'],errors='coerce')
    columna = pd.to_numeric(columna,errors='coerce')
    return columna

def normalizaColumna(datos,columna):
    datos[columna]= datos[columna]/datos[columna].max()
    return datos

def obtenerDummis(datos, columna):
    datos= pd.get_dummies(datos[columna])
    return datos

def renombrarColumna(datos,cambio):
    datos.rename(columns= cambio, inplace= True)
    return datos
    
    
if __name__ =="__main__":
    ruta='C:\\Users\\YENIFER\\.spyder-py3\\numpy\\datos\\'
    fichero = 'precios_carros.csv'
    datos = cargaDatos(ruta, fichero)
    print(datos.head(5))
    print(dameColumnas(datos))
    guardarDatos(datos, ruta, 'copia.csv')
    titulos_cabecera=['Indice', 'Nombre', 'Localización', 'Año', 'Kilometros', 'Tipo_Combustible', 'Transmisión', 'Propietario','Millage','Motor','Potencia','Asientos','Precio']
    cambiaColumnas(datos, titulos_cabecera)
    print(datos.columns)
    print("Estdisticos numericos")
    print(dameEstadisticos(datos))
    print("Estadisticos para todos")
    print(dameEstadisticos(datos, 'todos'))
    columna = datos['Precio']
    columna= cambiarTipo(columna,'int64')
    print(columna.dtype)
    print('Precio')
    print(columna)
    datos= renombrarColumna(datos, {'Precio':'precios'})
    print(datos.columns)
    datos= normalizaColumna(datos, 'precios')
    print(datos['precios'])