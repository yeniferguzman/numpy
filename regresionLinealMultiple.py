# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 14:31:59 2022

@author: YENIFER
"""

import modulo as md
import pandas as pd
import matplotlib.pyplot as plt


#cargo los datos
ruta = 'C:\\Users\\YENIFER\\.spyder-py3\\numpy\\datos\\'
fichero ='datos_modificados.csv'
datos = md.cargaDatos(ruta, fichero,",")
print(datos.head())

#columna indice
datos.set_index('indice', inplace=True)
print(datos.head())
#Columnas con valores nulos 
Columnas_nulos = [col for col in datos.columns if datos[col].isnull().any()]
print(Columnas_nulos)
#columnas 
print(md.dameColumnas(datos))
#Hot encoding
datos_dummies= md.obtenerDummis(datos, 'combustible')
print(datos_dummies.head())
datos= pd.concat([datos, datos_dummies],axis=1)
print(datos.columns)
datos_dummies= md.obtenerDummis(datos, 'kilometros')
print(datos_dummies.head())
datos= pd.concat([datos, datos_dummies],axis=1)
print(datos.columns)
datos_dummies= md.obtenerDummis(datos, 'localizacion')
print(datos_dummies.head())
datos= pd.concat([datos, datos_dummies],axis=1)
print(datos.columns)
datos= pd.concat([datos, datos_dummies],axis=1)
print(datos.columns)

#Normalización
datos= md.normalizaColumna(datos, 'año')
datos= md.normalizaColumna(datos, 'precios')

#prdicción y= a+b^x
from sklearn.linear_model import LinearRegression
#Creo la regresión lineal 
lm = LinearRegression()
#Defino variables predictoras y variables objetivo
x= datos[['año', 'precios','CNG', 'Diesel', 'LPG', 'Petrol', 'CNG',
'Diesel', 'LPG', 'Petrol', 'First',
'Fourth & Above', 'Second', 'Third', 'First', 'Fourth & Above',
'Second', 'Third', 'Ahmedabad', 'Bangalore',
'Chennai', 'Coimbatore', 'Delhi', 'Hyderabad', 'Jaipur', 'Kochi',
'Kolkata', 'Mumbai', 'Pune', 'Ahmedabad', 'Bangalore', 'Chennai',
'Coimbatore', 'Delhi', 'Hyderabad', 'Jaipur', 'Kochi', 'Kolkata',
'Mumbai', 'Pune']]
print(x)
y= datos['nuevo precio']

print(x)
print("*"*100)
print(y)
#Entrenamiento o ajuste
lm.fit(x,y)
#predicción
prediccion = lm.predict(x)
a= lm.intercept_
b = lm.coef_
#Muestro ecuacnión
#print(f'y = {a}+{b1}*x1+b2*x2+')
print("*"*100)
print('Predicción')
print(prediccion)
print(y)
print(lm.score(x , y))

#Creo un dataset  para comparar
resultado = {'Real': datos['nuevo precio'],'Predicción':prediccion}
R = pd.DataFrame(data=resultado)
print(R.head())

from sklearn import metrics
ECM= metrics.mean_squared_error(datos['nuevo precio'], prediccion)
print('Error cuadratico ',ECM)
r_cuadrado =  metrics.r2_score(datos['nuevo precio'], prediccion)
print('R cuadrado',r_cuadrado)

#Grafica 
#plt.plot(datos['combustible'], prediccion,'r', label='Prediccion')
plt.scatter(datos['combustible'], y, label = 'Datos')
plt.scatter(datos['combustible'], prediccion,c='red', label ='Prediccion')
plt.title('Regresión Lineal ')
plt.xlabel('combustible')
plt.xlabel('Y')
plt.legend()
plt.grid()
plt.show()












