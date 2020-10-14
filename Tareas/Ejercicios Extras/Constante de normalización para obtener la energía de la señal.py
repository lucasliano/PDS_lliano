# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 17:45:10 2020

@author: LucasLiaño
"""

#%% Agrego librería propia al path
import sys
sys.path.append('D:/LucasLiaño/Escritorio/Lucas/UTN/PSD/Tareas (Spyder)')


#%% Importo librerías
import numpy as np
import matplotlib.pyplot as plt


#%%
import myLibrary as my

fs = 1000
N = 1000
W = fs/N

A = 2

t1,f1 = my.SignalGenerator ('sin',(100, A) ,fs, N, (0, 0));
k1, Fk1, kk1, Fkk1 = my.DFT(f1, N, W, escala='p');

# Si queremos que se cumpla Parserval (Es decir que la potencia en t y en w sean iguales)
# se va a tener que cumplir que la sumatoria del modulo cuadrado en t sea igual a la sumatoria en modulo 2 en w


potf = np.mean(f1**2)
potw = np.sum(np.abs(Fkk1)**2)
cte = potw/potf

# Vemos que coincide la potencia porque multiplicamos por un factor de raiz de 2 en Fkk
# Pero vemos que no coincide la amplitud

plt.figure(1)
plt.plot(np.abs(Fkk1))