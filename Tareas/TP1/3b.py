# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 17:55:01 2020

Ejercicio 3.a:
    Verifique qué ocurre si a la señal de $f_0 = f_S/4 + 0.5$ se le agregan ceros para prolongar su duración. Es decir si la señal tiene N muestras, agregue $M_j$ ceros siendo $M_j = ( \frac{N}{10},\, N,\, 10N)$
    

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
tus_resultados = [ ['$ \lvert X(N/4) \lvert$', '$ \lvert X(N/4 + 1) \lvert $', '$\sum_{i=F} \lvert X(f_i) \lvert ^2 $'], 
                   [''                       , ''                          , '$F:f \neq N/4$'                       ] 
                 ]

# Inicializamos la entidad loopeable.
Mj = (0, N/10, N, 10*N)




for each in Mj:
    foL = fs/4 + 0.5
    W = fs/(N+each)
    tL,fL = my.SignalGenerator ('sin',(foL, 1), fs, N, (0, 0));
    
    fL = np.pad(fL, (0, int(each)), mode='constant', constant_values = (0,0))    #Add zero padding
    kL, FkL, kkL, FkkL = my.DFT(fL, int(N+each), W);
    
    fig, axs = plt.subplots(1)
                      
    axs.plot(fL) 
    axs.set_xlabel('Tiempo [n*Ts]')  
    axs.set_ylabel('Amplitud [V]')  
    axs.set_title("Analisis temporal") 
                  
    
    
    fig, axs = plt.subplots(1)
                      
    axs.stem(kkL* W, np.abs(FkkL), use_line_collection = True) 
    axs.set_xlabel('Frecuencia [k*W]')  
    axs.set_xlim(N/4 - 5, N/4 + 5)
    axs.set_ylabel('Amplitud [V]')  
    axs.set_title("Módulo") 
                  
 
    tus_resultados.append([ (np.abs(FkkL[int( N/4)    ]) ), 
                            (np.abs(FkkL[int( N/4) + 1]) ),
                            (np.sum(np.abs(FkkL)**2) - (np.abs(FkkL[int( N/4)])**2))   
                          ])
    
df = DataFrame(tus_resultados, columns=['Frecuencia central', 'Primer adyacente', 'Resto de frecuencias'],
               index=['$M_j$ \ expr. matemática', 
                      '',
                      '0', 
                      '$N/10$', 
                      '$N$', 
                      '$10N$'])
    
    
    
    
    
    
    
    
    