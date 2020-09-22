# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 17:55:01 2020

Ejercicio 3.a:
    Verifique el efecto del leakage para una senoidal de $f_0 = f_S/4 + f_D$ siendo $f_D = (0.01,\, 0.25,\, 0.5)$, es decir una frecuencia de desintonía respecto al bin $f_S/4
    

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

fs = 50
N = 50

#%% Cosas propias del ejercicio :D

# Inicializamos las variables donde vamos a almacenar los datos :D
tus_resultados = [ ['$ \lvert X(f_0) \lvert$', '$ \lvert X(f_0+1) \lvert $', '$\sum_{i=F} \lvert X(f_i) \lvert ^2 $'], 
                   [''                       , ''                          , '$F:f \neq f_0$'                       ] 
                 ]

# Inicializamos la entidad loopeable.
fd = (0, 0.01, 0.25, 0.5)

W = fs/N

for each in fd:
    foL = fs/4 + each
    tL,fL = my.SignalGenerator ('sin',(foL, 1), fs, N, (0, 0));
    kL, FkL, kkL, FkkL = my.DFT(fL, N);
    
    fig, axs = plt.subplots(1,2)
                      
    axs[0].stem(kkL* W, np.abs(FkkL), use_line_collection = True) 
    axs[0].set_xlabel('Frecuencia [k*W]')  
    axs[0].set_ylabel('Amplitud [V]')  
    axs[0].set_title("Módulo") 
                  
    axs[1].stem(kkL* W, np.angle(FkkL), use_line_collection = True)
    axs[1].set_xlabel('Frecuencia [k*W]')  
    axs[1].set_ylabel('Amplitud [V]')  
    axs[1].set_title("Fase") 
    
    # Nota: Voy a escalar todas las componentes en 2/N para que me quede representada la energía
    tus_resultados.append([ (np.abs(FkL[int(foL)  ]) * 2/N), 
                            (np.abs(FkL[int(foL)+1]) * 2/N),
                            ((np.sum(np.abs(FkL)**2) - (np.abs(FkL[int(foL)])*2)) * 2/N)  
                          ])
    
df = DataFrame(tus_resultados, columns=['Frecuencia central', 'Primer adyacente', 'Resto de frecuencias'],
               index=['$f_0$ \ expr. matemática', 
                      '', 
                      '$f_S/4$', 
                      '$f_S/4+0.01$', 
                      '$f_S/4+0.25$', 
                      '$f_S/4+0.5$'])
    
    
    
    
    
    
    
    
    
    
    