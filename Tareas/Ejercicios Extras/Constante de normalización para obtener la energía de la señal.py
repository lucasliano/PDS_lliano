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
import matplotlib as plt


#%%
import myLibrary as my

fs = 1000
N = 1000
W = fs/N

t1,f1 = my.SignalGenerator ('sin',(100, 1) ,fs, N, (0, 0));
k1, Fk1, kk1, Fkk1 = my.DFT(f1, N, W);

# Si queremos que se cumpla Parserval (Es decir que la potencia en t y en w sean iguales)
# se va a tener que cumplir que la sumatoria del modulo cuadrado en t sea igual a la sumatoria en modulo 2 en w

cte = np.sum(f1**2)/ np.sum(np.abs(Fk1)**2)

# sum f[n] = cte * sum Fk[k]

# Vemos que cte se aproxima a 1/N (Debe haber alguna falla en algun lado y no se donde :D)