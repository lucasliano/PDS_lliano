# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 17:15:52 2020

Prueba: Convolución entre kernels de Dirichlet


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

N = 1000
fs = 1000

#%% Procesamiento

# We create the temporal axis
nts = np.arange(-10, 10, 1/fs)

# This is the first Dirichlet Kernel, according to a rectangular pulse with N1 points
N1 = 1000
kd1 = np.sin(np.pi * nts) / np.sin((np.pi/N1) * nts)

# This is the first Dirichlet Kernel, according to a rectangular pulse with N1 points
N2 = 500
kd2 = np.sin(np.pi * nts) / np.sin((np.pi/N2) * nts)


kdconv = np.convolve(kd1,kd2,'same')

#%% Plotting

plt.figure(1)
plt.plot(nts,kd1)
plt.title('$D_{1000}$ Dirichlet kernel')

plt.figure(2)
plt.plot(nts,kd2)
plt.title('$D_{500}$ Dirichlet kernel')

plt.figure(3)
plt.plot(nts, kdconv)
plt.title('$D_{?}$ Dirichlet kernel')


