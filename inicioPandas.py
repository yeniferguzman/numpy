# -*- coding: utf-8 -*-
"""
Created on Wed Aug 17 11:57:19 2022

@author: YENIFER
"""

import pandas as pd
import numpy as np
#SERIES
#etique = ['a', 'b', 'c', 'd', 'e']
#datos= np.arange(4, 9)
#serie =pd.Series(datos, index=etique)
#print(serie)
#acceder a valor 
#print(serie['c'])
#Datos e distintos tipos
#print("Serie con diferentes tipos de datos")
#datos=['Yenifer', 37, "Sneyder",46.5]
#se crea otra serie
#serie= pd.Series(datos)
#print(serie)

#datos directos
#seried= pd.Series([1000, 500, 300, 400],['emp01', 'emp02', 'emp03', 'emp04'])
#print(seried)

#operaciòn suma
#serie1 = pd.Series([200, 500, 300, 400],['emp01', 'emp02', 'emp03', 'emp04'])
#print(serie1)
#serie2 = pd.Series([100, 800, 600, 700],['emp01', 'emp02', 'emp03', 'emp04'])
#print(serie2)
#serie3 = serie1+ serie2
#print("Suma de serie: ",serie3)

#DATAFRAMES: los datos se organizan por filas y columnas
filas= ['tienda1', 'tienda2', 'tienda3', 'tienda4']
columna=['articulo1', 'articulo2', 'articulo3']
datos= [[np.nan,100,1200],[np.nan,100,300],[300,np.nan,400],[400,100,500]]

dataframe = pd.DataFrame(datos, index=filas, columns = columna)
print(dataframe)
print("---------------------------")
#seleccion fila- loc porque no uso el indice
print(dataframe.loc['tienda2'])
print("---------------------------")
print(dataframe.loc[['tienda2','tienda3']])
print("---------------------------")
#Seleccciono columna= es decir el articulo x
print(dataframe['articulo3'])
print("---------------------------")
#valor concreto se indica fila y columna
#print(dataframe.loc['tienda2', 'articulo3'])
#AÑADIR UNA COLUMNA
dataframe ['articulo4'] = 25
#print(dataframe)
#dataframe['total']= dataframe['articulo1']+dataframe['articulo2']+dataframe['articulo3']+dataframe['articulo4']
#print(dataframe)
#eliminar columna- axis para que indicar que es una columna
#Si lo dejo hasta axis= 1 oculta la columna al momento de imprimir
#inplace indica que luego de eliminar guarde en dataframe
#print(dataframe.drop(['total'], axis = 1,  inplace=True))
#print(dataframe)
#imprimir una parte de dataframe, para este ejem solo los que cumplen la condiciòn
#condicion = dataframe >200
#print(dataframe[condicion])
#condicion = (dataframe['articulo1'] >= 200)&(dataframe['articulo2']>= 100)
#print(dataframe[condicion])
#split corta por espacio y devuelve la lista, por eso no uso []
nuevaColumna='1 2 3 4'.split()
dataframe['indices']= nuevaColumna
print(dataframe)
#paso los indices a la primera columna
dataframe= dataframe.set_index('indices')
print(dataframe)
#agrego a datos valores nulos con np.nan, y elimino las columnas que tengan valores nulos
#dataframe.dropna(axis=1, inplace=True)
#print(dataframe)
#relleno los valores nulos  con fillna
#dataframe.fillna(value=90, inplace=True)# opcion 1
media= dataframe.mean()
#relleno los valores nulos con el valor de la media que le corresponden a cada columna
print(f"La media es = {media}")
dataframe.fillna(value=media, inplace=True)
print(dataframe)
#union de dataframe
data1 = dataframe.copy()
data2 = dataframe.copy()
print(data1)
print(data2)
dataTotal= pd.concat([data1, data2],axis=0)#axis porque lo imprimo por columna
print(dataTotal)
#elementos únicos
print(dataTotal['articulo3'].unique())
#funcion value_counts para contar cuantas veces se repite un valor
print(dataTotal['articulo3'].value_counts())

dataTotal = dataTotal.apply(lambda x: x*3)
print(dataTotal)

#obtener columnas 
print(dataTotal.columns)
print(dataTotal.index)
#Funcion sort_values ordena por articulo
print(dataTotal.sort_values(['articulo3']))
#obtener estadistica con la función describe()
print("Datos Estadisticos")
print(dataTotal.describe())

#pasar el dataframe a un archivos csv
#dataTotal.to_csv('dataTotal.cvs') #guarda
#cargar cvs:actualizo el archivo y al ejecutar la siguiente linea se imprime la modificación
dataframe= pd.read_csv('dataTotal.cvs',index_col=0)
print(dataframe)




