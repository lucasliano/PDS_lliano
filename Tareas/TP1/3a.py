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

fs = 500
N = 500

#%% Cosas propias del ejercicio :D

# Inicializamos las variables donde vamos a almacenar los datos :D
tus_resultados = [ ['$ \lvert X(f_0) \lvert$', '$ \lvert X(f_0+1) \lvert $', '$\sum_{i=F} \lvert X(f_i) \lvert ^2 $'], 
                   [''                       , ''                          , '$F:f \neq f_0$'                       ] 
                 ]

# Inicializamos la entidad loopeable.
fd = (0, 0.01, 0.25, 0.5)



for each in fd:
    foL = fs/4 + each
    tL,fL = my.SignalGenerator ('sin',(foL, 1), fs, N, (0, 0));
    kL, FkL, kkL, FkkL = my.DFT(fL, N);
    
    fig, axs = plt.subplots(1,2)
                      
    axs[0].stem(kkL, np.abs(FkkL)) 
    axs[0].set_xlabel('Frecuencia [k*W]')  
    axs[0].set_ylabel('Amplitud [V]')  
    axs[0].set_title("Módulo") 
                  
    axs[1].stem(kkL, np.angle(FkkL))
    axs[1].set_xlabel('Frecuencia [k*W]')  
    axs[1].set_ylabel('Amplitud [V]')  
    axs[1].set_title("Fase") 
    
    #tus_resultados.append([])
    
    
    
    
    
    
    
    
    
    
    
    