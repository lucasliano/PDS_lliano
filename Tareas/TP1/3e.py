# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 17:55:01 2020

Ejercicio 3.e:
    Analice cuál es la frecuencia  $\hat{f}_0 = \mathop{arg\ max}_f \{\lvert X(f) \rvert \}$ a la que ocurre el máximo del espectro y en cuánto difiere de $f_0$ en términos porcentuales

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

# Inicializamos las variables donde vamos a almacenar los datos :D
tus_resultados = []

# Inicializamos la entidad loopeable.
Mj = (0, N/10, N, 10*N)

for each in Mj:
    foL = fs/4 + 0.5
    W = fs/(N+each)
    tL,fL = mySignalGenerator ('sin',(foL, 1), fs, N, (0, 0));
    
    fL = np.pad(fL, (0, int(each)), mode='constant', constant_values = (0,0))    #Add zero padding
    
    kL, FkL, kkL, FkkL = mi_analizador(fL, int(N+each), W);
                      
 
    tus_resultados.append([ np.argmax(FkkL) ])
    
#tus_resultados = (tus_resultados + tus_resultados[0]) * 100

df = DataFrame(tus_resultados, columns=['$e_\%$'],
               index=['0',
                      '$N/10$', 
                      '$N$', 
                      '$10N$'])
    
    
    
    
    