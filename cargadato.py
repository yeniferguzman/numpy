# -*- coding: utf-8 -*-
"""
Created on Mon Aug 29 10:14:17 2022

@author: YENIFER
"""

import pandas as pd

fichero = pd.read_csv(r'C:\Users\YENIFER\.spyder-py3\numpy\datos\precios_carros.csv')
datos = (fichero)
#si el archivo csv no tiene cabecero se le agrega usando header=None
#print(datos)

print(datos.head(5))
print("*"*10)
print(datos.tail(6))

#Imprimir titulos de columnas
print(datos.columns)
#Creo una lista para cambiar los titulos de las columnas
titulos_cabecera=['Indice', 'Nombre', 'Localización', 'Año', 'Kilometros', 'Tipo_Combustible', 'Transmisión', 'Propietario','Millage','Motor','Potencia','Asientos','Precio']
datos.columns = titulos_cabecera
print(datos.head(5))
print(datos.columns)

#Exportar datos en diferentes formatos
fichero =pd.read_csv(r'C:\Users\YENIFER\.spyder-py3\numpy\datos\precios_carros.csv')
datos.to_csv(fichero)