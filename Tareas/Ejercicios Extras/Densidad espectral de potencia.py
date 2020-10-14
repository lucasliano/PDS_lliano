# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 11:59:07 2020

En este documento mostramos como calcular la potencia de un ruido blanco Gaussiano a partir
de la secuencia de autocorrelación

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

N = 1000
fs = 1000
W = fs/N

#%% Comienza el ejercicio

sigma = np.sqrt(1/10)   # sigma^2 = 1/10 

n = np.random.normal(0, sigma, N)

# La potencia la podemos calcular temportalmente como la media de f(t)**2
Potencia_del_ruido_temporal = np.mean(n**2)

# Nota: Es necesario normalizar esta secuencia dado que la función de salida depende del 
#       tamaño de la señal.
gaussianNoiseCorrelation = np.correlate(n, n, 'same') * (1/N)   # Normalizo la secuencia de autocorrelación

k, Fk, kk, Fkk = my.DFT(gaussianNoiseCorrelation, N, nombre='$r(\tau)$', escala='a') # Pido que se mantengan las unidades de amplitud

# En este caso, como la secuencia resultante de la DFT es una densidad espectral de potencia
# para calcular la potencia debemos integrar la misma, no su módulo cuadrado.
Potencia_del_ruido_densidad_espectral = np.sum(np.abs(Fkk))


# Finalmente, podemos calcular la potencia como hacemos con cualquier otra señal, a partir
# de la relación de Parseval. Para ello hacemos la sumatoria del módulo**2 de la DFT de la señal
# NO DE SU AUTOCORRELACIÓN!!!

k, Fk, kk, Fkk = my.DFT(n, N, escala='p') # Pido que se mantengan las unidades de potencia

Potencia_del_ruido_frecuencia = np.sum(np.abs(Fkk)**2)
#%% Plotting

fig = plt.figure(3)
axs = fig.add_subplot(1, 1, 1)
axs.plot(gaussianNoiseCorrelation)
axs.set_xlabel('Retardo [tau]')  
axs.set_ylabel('Amplitud [V]')  
axs.set_title("Autocorrelación del ruido de gaussiano") 
axs.grid()
  
fig = plt.figure(4)
axs = fig.add_subplot(1, 1, 1)                  
axs.plot(kk* W, my.to_db(np.abs(Fkk))) 
axs.set_xlabel('Frecuencia [k*W]')
axs.set_ylabel('Amplitud [dB]')  
axs.set_title("Módulo") 
axs.grid()
  

              


