# -*- coding: utf-8 -*-
"""
Created on Fri Aug 26 15:04:44 2022

@author: YENIFER
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

x= np.linspace(1,150,200)
y = x + x**2
#print(x)
#print(y)
plt.plot(x,y, 'blue')
plt.title('Mi grafico')
plt.xlabel('Valores X')
plt.ylabel('Valors Y')
plt.show()
#subplot- dos graficas 
plt.subplot(1,2,1)
plt.plot(x,y,'g')
plt.subplot(1,2,2)
plt.plot(x,y,'red')
plt.show()
