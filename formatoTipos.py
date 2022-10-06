# -*- coding: utf-8 -*-
"""
Created on Fri Sep  2 09:34:24 2022

@author: YENIFER
"""

import pandas as pd
import numpy as np

fichero = pd.read_csv(r'C:\Users\YENIFER\.spyder-py3\numpy\datos\precios_carros.csv')
datos =(fichero)
print(datos.head())

print(datos.dtypes)
#Cambio tipo de datos
datos['Unnamed: 0'] = datos['Unnamed: 0'].astype('float64')
print(datos.dtypes)

#realizo calculos y ponerlos en otra columna
#millas = kilometros * 0.621371
datos['millas_driven']= datos['Kilometers_Driven']*0.621371
print(datos.head())

#renombro columna
datos.rename(columns={'millas_driven':'Millas'},inplace=True)
print(datos.head())

#Noramlizar los datos
#Minimo y valor anterior
print(datos[['Millas','Kilometers_Driven']])
datos['Millas_normatizadas']= datos['Millas']/datos['Millas'].max()
datos['Kilometros_normatizados']= datos['Kilometers_Driven']/datos['Kilometers_Driven'].max()
print(datos[['Millas_normatizadas','Kilometros_normatizados']])

#min, max
print(datos[['Millas','Kilometers_Driven']])
datos['Millas_normatizadas']=(datos['Millas']-datos['Millas'].min())/(datos['Millas'].max()-datos['Millas'].min())
datos['Kilometros_normatizados']= (datos['Kilometers_Driven']-datos['Kilometers_Driven'].min())/(datos['Kilometers_Driven'].max()-datos['Kilometers_Driven'].min())
print(datos[['Millas_normatizadas','Kilometros_normatizados']])