# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 00:51:09 2020

Resumen: En este ejercicio se van a simular multiples corridas del espacio de muestras para el ruido. De esta manera vamos a comparar 

@author: LucasLiaño
"""
#%% Se importan libreriras adecuadas
import numpy as np
import matplotlib.pyplot as plt
import myLibrary as my

fs = 1000
N = 1000
W = fs/N


# Genero el plot
fig, (ax5,ax2) = plt.subplots(1,2)
ax5.set_xlabel('Retardo [ tau ]')  
ax5.set_ylabel('Amplitud [V]')  
ax5.set_title("Correlación ruido blanco") 

ax2.set_xlabel('Frecuencia [k*W]')  
ax2.set_ylabel('Amplitud [V]')  #Debería ser sigma^2/N porque el area en t es sigma^2 y la base es N.
ax2.set_title("Análisis en frecuencia") 

# Genero las señales a plottear
for i in range(0,1000,100):
    t2,f2 = my.SignalGenerator ('n',(0, 1) ,fs, N + i, (0, 0));
    k2, Fk2, kk2, Fkk2 = my.DFT(f2, N + i);
    ax5.plot(t2 - (N+i)/(2*fs), np.correlate(f2,f2,'same'), label='Ruido N = 1000+'+str(i))  #Hay que escalar esto. 
    ax2.plot(kk2*W, np.abs(Fkk2), label='Ruido con $\sigma$ = '+str(np.std(f2)) )  #Hay que escalar esto. 


ax5.legend() 
ax2.legend()