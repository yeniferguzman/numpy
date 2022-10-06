# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 15:36:01 2022

@author: YENIFER
"""

import pandas as pd

fichero = pd.read_csv(r'C:\Users\YENIFER\.spyder-py3\numpy\datos\precios_carros.csv')
datos = fichero
print(datos.columns)
print(datos['Fuel_Type'])

#convertir variable catergorica en dummies o ficticia
columna_dummies = pd.get_dummies(datos['Fuel_Type'])
print(columna_dummies)

#Creo el datasset
datos_dummies = pd.get_dummies(datos,columns= ['Fuel_Type'])
print(datos.head)
print('*'*25)
print('*'*25)
#↓Imprimo el nuevo datasset con las variables dummies
print(datos_dummies.head())