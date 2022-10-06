# -*- coding: utf-8 -*-
"""
Created on Thu Sep 29 15:59:36 2022

@author: YENIFER
"""

import modulo as md


#cargo los datos
ruta = 'C:\\Users\\YENIFER\\.spyder-py3\\numpy\\datos\\'
fichero ='datos_modificados.csv'
datos = md.cargaDatos(ruta, fichero,",")
print(datos.head())

#columna indice
datos.set_index('indice', inplace=True)
print(datos.head())

#prdicción y= a+b^x
from sklearn.linear_model import LinearRegression

#Creo la regresión lineal 
lm = LinearRegression()
#Defino variables predictoras y variables objetivo
x= datos[['año']]
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
print(f'y = {a}+{b}*x')
print("*"*100)
print('Predicción')
print(prediccion)
print(y)
print(lm.score(x , y))
#Visulización
import seaborn as sns
sns.regplot(x='año', y= 'nuevo precio', data =datos)
#cisualizar revisión-predicción -error
sns.residplot(datos['año'],datos['nuevo precio'])

#separando entrenamiento y pruebas 
#Defino variables predictoras y variables objetivo
x= datos[['año']]
y= datos['nuevo precio']
#Separo entrenamiento y prueba 
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=0.2, random_state=0)

print(x_train)
print("*"*100)
print(y_train)
#Entrenamiento o ajuste
lm.fit(x_train,y_train)
#predicción
prediccion = lm.predict(x_test)
a= lm.intercept_
b = lm.coef_
#Muestro ecuacnión
print(f'y = {a}+{b}*x')
print("*"*100)
print('Predicción')
print(prediccion)
print(y_test)
print(lm.score(x_train , y_train))
#Visulización
import seaborn as sns
sns.regplot(x='año', y= 'nuevo precio', data =datos)
#cisualizar revisión-predicción -error
sns.residplot(datos['año'],datos['nuevo precio'])

