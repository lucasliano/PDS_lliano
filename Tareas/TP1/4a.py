# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 17:55:01 2020

Ejercicio 4.a:
    Senoidal de **energía normalizada** y frecuencia $f_0 = 9 \cdot f_S/N$

@author: LucasLiaño
"""

#%% Agrego librería propia al path
import sys
sys.path.append('D:/LucasLiaño/Escritorio/Lucas/UTN/PSD/Tareas (Spyder)')

#%% Declaración del ejercicio.. Estas son cosas que ya estan definidas
##  en el notebook.
import myLibrary as my
import matplotlib.pyplot as plt
import numpy as np
from pandas import DataFrame

fs = 1000
N = 1000

#%% Cosas propias del ejercicio :D

#Inicializamos las variables donde vamos a almacenar los datos :D
tus_resultados = [ ['$\sum_{f=0}^{f_S/2} \lvert X(f) \rvert ^2$', '$ \lvert X(f_0) \rvert ^2 $', '$ \mathop{arg\ max}_f \{\lvert X(f) \rvert ^2\} $'], 
                    ['',                                     '',                           '$f \in [0:f_S/2]$'], 
                    [ '', '','']
                  ]
tus_resultados.append(['1', '1', '9'])
tus_resultados.append([ '', '',''])



W = fs/N
fo = 9 * W
A = np.sqrt(6) 

t,f = my.SignalGenerator ('sin',(fo, A), fs, N, (0, 0));


k, Fk, kk, Fkk = my.DFT(f, N, W);

fig, axs = plt.subplots(1)
                      
axs.plot(f) 
axs.set_xlabel('Tiempo [n*Ts]')  
axs.set_ylabel('Amplitud [V]')  
axs.set_title("Análisis temporal") 
              
fig, axs = plt.subplots(1)
                  
axs.stem(kk* W, np.abs(Fkk), use_line_collection = True) 
axs.set_xlabel('Frecuencia [k*W]')
axs.set_ylabel('Amplitud [V]')  
axs.set_title("Módulo") 

tus_resultados.append([ (np.mean((f)**2)    ), 
                        (np.sum(np.abs(Fkk)**2)    ), 
                        (np.abs(Fkk[int(fo)])**2    ),
                        (np.argmax(np.abs(Fkk)**2)  )   
                      ])




df = DataFrame(tus_resultados, columns=['Energía total', 'Energía en $f_0$', 'Máximo de Energía'],
               index=['$f_0$ \ expr. matemática', 
                      '', 
                      '', 
                      'predicción', 
                      '', 
                      'simulación'])
    
    

    
    