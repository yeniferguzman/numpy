# -*- coding: utf-8 -*-
"""
Created on Thu Sep  8 15:49:39 2022

@author: YENIFER
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

fichero = pd.read_csv(r'C:\Users\YENIFER\.spyder-py3\numpy\datos\precios_carros.csv')
datos = fichero

print(datos.columns)
titulos_cabecera=['Indice', 'Nombre', 'Localización', 'Año', 'Kilometros', 'Tipo_Combustible', 'Transmisión', 'Propietario','Millage','Motor','Potencia','Asientos','Precio']
datos.columns = titulos_cabecera
print(datos.head(5))
print(datos.columns)
intervalo = np.linspace(min(datos['Kilometros']),max(datos['Kilometros']),4)
nombre_grupos = ['pocos','normal','muchos']

#Utilizo cut para ordenar
datos['Kilometros_agrupados']= pd.cut(datos['Kilometros'],intervalo,labels=nombre_grupos,include_lowest=True)
print(datos['Kilometros_agrupados'])
plt.hist(datos['Kilometros'],bins=intervalo, rwidth=0.5, color='#991')
plt.title('Histograma Kilometros')
plt.xlabel('Kmts')
plt.ylabel('Frecuencia')
plt.show()