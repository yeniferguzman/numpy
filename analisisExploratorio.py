# -*- coding: utf-8 -*-
"""
Created on Tue Sep 20 08:51:25 2022

@author: YENIFER
"""

import modulo as md
import matplotlib.pyplot as plt

#cargar datos
ruta = 'C:\\Users\\YENIFER\\.spyder-py3\\numpy\\datos\\'
fichero ='precios_carros.csv'
datos = md.cargaDatos(ruta, fichero)
print(datos.head())

#Columna Indice
datos.set_index('Unnamed: 0', inplace=True)
#print(datos.head())
#renompro columna 
datos.index.name = 'indice'
print(datos.head())
#+Cambio nombre de columnas
print(md.dameColumnas(datos))
nombre_columnas = ['nombre', 'localizacion', 'año', 'kilometros Recorridos', 'combustible', 'tipo propietario', 'kilometros','motor', 'potencia', 'asientos', 'nuevo precio', 'precios']
md.cambiaColumnas(datos, nombre_columnas)
print(md.dameColumnas(datos))
#Estadisticps basicos
print(md.dameEstadisticos(datos))
print('*'*100)
print(md.dameEstadisticos(datos, 'all'))
#Valores nulos
datos = md.reemplazarNulos(datos, 'nuevo precio')
print(md.dameEstadisticos(datos))
#cambbio tipo de dato
datos['motor']=md.cambiarTipo(datos['motor'])

print('nuevo precio')
print(datos['nuevo precio'])
datos['nuevo precio']=md.cambiarTipo(datos['nuevo precio'])
datos = md.reemplazarNulos(datos, 'nuevo precio')
print('año')
print(datos['año'])
print(datos.info)
#contar cuantas veces aparece un nombre
print(datos['nuevo precio'].value_counts())
plt.boxplot(datos['nuevo precio'])
plt.title('Nuevo precio')
plt.show()
#GRafico de dispersión relación entre variables
y= datos['nuevo precio']
x= datos['año']
plt.scatter(x, y)
plt.title('Nuevo precio / año')
plt.xlabel('Nuevo precio')
plt.ylabel('año')
plt.show()

#Mediante coeficiente de correlación y /o valor 
#Si prox a 1 relación positiva
#Si prox a -1 relación negativa
#Si prox a 0 sin relación
#P valor
#Si <0.001 fuerte certeza en el resultado 
#Si <0.005 sera moderado
#Si <0.1 baja o debil
#si >0.1 sin certeza de correlación

from scipy import stats
datos=md.reemplazarNulos(datos,'nuevo precio')
datos=md.reemplazarNulos(datos, 'año')
datos['precios']=md.cambiarTipo(datos['nuevo precio'])

pearson_coef, p_valor = stats.pearsonr(datos['nuevo precio'], datos['año'])
print(f'El coeficiente de correlación de Pearson es: {pearson_coef}')
#obtener el P valor
print(f'El P valor es: {p_valor}')



fichero='datos_modificados.csv'
md.guardarDatos(datos, ruta, fichero)