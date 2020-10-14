# -*- coding: utf-8 -*-
"""
Created on Sat Oct  3 11:57:01 2020

Ejercicio 5:
    Simule el efecto de cuantizar una señal continua en el tiempo mediante un conversor analógico digital (ADC).

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

plt.close('all')


N1 = int(1e4)
fs1 = int(1e4)

#%% Comienza el ejercicio

# Variables del ADC
nbits = 8
pVref = 5
nVref = -5
fsADC = int(1e3)

# Relacionado a señales
W = fs1/N1
fo = 5
A = np.sqrt(2)          # Esto tiene potencia unitaria. 

sigma = np.sqrt(1/10)   # sigma^2 = 1/10 


# Comienza procesamiento de datos
t,f = my.SignalGenerator ('sin',(fo, A), fs1, N1, (0, 0))

n = np.random.normal(0, sigma, N1)
gaussianNoiseCorrelation = np.correlate(n, n, 'same') * (1/N1)   # Normalizo 


fr = f + n

tsampled, fsampled , Qi = my.ADC(fr,t ,fsADC, nbits, pVref, nVref)
NADC = np.size(tsampled)
W = fsADC/NADC

quantizationNoiseCorrelation = np.correlate(Qi, Qi, 'same') * (1/NADC) # Normalizo


k, Fk, kk, Fkk = my.DFT(Qi, NADC, escala='a')


Potencia_del_ruido_temporal = np.mean(n**2)
Potencia_del_ruido_frecuencia = np.sum(np.abs(Fkk))

#%% Plotting

fig = plt.figure(3)
axs = fig.add_subplot(1, 1, 1)
axs.plot(Qi)
axs.set_xlabel('Retardo [tau]')  
axs.set_ylabel('Amplitud [V]')  
axs.set_title("Autocorrelación del ruido de cuantización") 
axs.grid()
axs.legend()
  
fig = plt.figure(4)
axs = fig.add_subplot(1, 1, 1)                  
axs.plot(kk* W, my.to_db(np.abs(Fkk))) 
axs.set_xlabel('Frecuencia [k*W]')
axs.set_ylabel('Amplitud [dB]')  
axs.set_title("Módulo") 
axs.grid()

plt.figure(5)
plt.plot(n)
plt.title('Gaussian noise w/ $\sigma$ = ' + str(np.std(n) ))
              




















