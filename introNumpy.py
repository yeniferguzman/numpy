# -*- coding: utf-8 -*-
"""
Created on Fri Aug 12 11:27:37 2022

@author: YENIFER
"""
import numpy as np
#Libreria numpy para operar vectores y matrices
lista1= [1,2,3,4,5,6,3,2,8,9]
#convertir la lista en una matriz utilizando array
# array = np.array(lista1)
# print(lista1)
# print(type(array))
# print(array)
# lista2= [[1,2],[2,5,3],[9,4,2]]
# array2 = np.array(lista2)
# print("Matriz",array2)

#llenar arrays automatica
# array = np.arange(2,15,2)
# print(array)
# matrizCeros = np.zeros((4,5))
# print(matrizCeros)
#Matriz de unos
# matrizUnos = np.ones((3,5))
# print((matrizUnos))

#matriz 40 elementoscon valores del 2 al 6
# matriz = np.linspace(2,6,40)
# print(matriz) 

#matriz identidad
# matrizIdentidad = np.eye(7)
# print(matrizIdentidad)

#matriz numeros aleatorios
matrizAleatoria = np.random.rand(3,4)
# print(matrizAleatoria)
# matrizAleaNormal = np.random.randn(4)
# print(matrizAleaNormal)

#matriz numeros enteros aleatorios 
# matrizAleaEnteros= np.random.randint(1,21,10)
# print(matrizAleaEnteros)

#tamaño Array 
array = np.random.randint(1,201,30)
print(array)
#La función reshape cambia la forma y se debe tener encuenta
#que el numero de filas por columnas debe dar el total de elementos definidos en el array
matriz = array.reshape(5,6)
print(matriz)

#operacines con 'matri'zes
'''print("matriz principal",matriz)
print("Rebanada 1 de matriz ",matriz[0])#PRIMERA FILA
print("Rebanada 2 de matriz ",matriz[:2])#rebanada hasta la 2 indice
print("Rebanada 3 de matriz ",matriz[1][2])#rebana
print("toda la segunda columna",matriz[:, 1])#imprimetoda la fila segunda columna
print("Toda la primera columnas",matriz[:, :1])#desde el inicio y las dos primeras columnas'''
print(matriz)
#print("suma de matriz",matriz + 10)
#print(matriz+ matriz)
#print(matriz*10)#multiplica cada valor por 10
#print(matriz*matriz)
#print("Numero maximo: ",np.max(matriz))
''''condicion =  matriz > 100
print(matriz)
print("condición ",condicion)
print("Muestra los valores que cumplen la condición: ",matriz[condicion])'''
#numeros impares
#condicion= (matriz % 2 != 0)
#print("Valores impares: ",matriz[condicion])#Devuelve todos lo numeros impares de la matriz original

#valores del 5 al  40
'''lista =np.arange(5,41)
print("Nueva lista: ",lista)
lista= lista.reshape(3,12)#se redimendiona a 3 filas 12 columnas
print("Matriz 3f 12 col ",lista)
print("Mostrar el valor indice 2,4 de la lista")
print(lista[2,4])'''

#combinación primitiva
arrayprimitiva = np.random.randint(1,50,6)
print(f"LA combinación gnadora será {arrayprimitiva}")


#Numeros max y min
# array = np.random.randint(1,901,200)
# print(array)
# maximo = array.max()
# print(f"el valor máximo es:{maximo}")
# print(array.argmax())#indica la posición donde se encuentra el numero máximo
# minimo = array.min()
# print(f"El valor minimo es {minimo}")
# print(array.argmin())

#mostrar elementos 
#array = np.arange(1,11)
# print(array)
#imprimo el 3 elemento
#print(array[2])
#imprimo desde un determinado elemento al último
#print(array[5:])
#imprimo desde el inicio hasta el elemento que le indique
#print(array[:6])





