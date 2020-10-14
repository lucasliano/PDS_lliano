# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 01:36:38 2020

@author: LucasLiaño
======================================================
Consigna:
    En este primer trabajo comenzaremos por diseñar un generador de señales que utilizaremos en las primeras simulaciones que hagamos. La primer tarea consistirá en programar una función que genere señales senoidales y que permita parametrizar:

    la amplitud máxima de la senoidal (volts)
    su valor medio (volts)
    la frecuencia (Hz)
    la fase (radianes)
    la cantidad de muestras digitalizada por el ADC (adim.)
    la frecuencia de muestreo del ADC.
    es decir que la función que uds armen debería admitir se llamada de la siguiente manera
    
    tt, xx = mi_funcion_sen( vmax = 1, dc = 0, ff = 1, ph=0, nn = N, fs = fs)
    Recuerden que tanto xx como tt deben ser vectores de Nx1. Puede resultarte útil el módulo de visualización matplotlib.pyplot donde encontrarán todas las funciones de visualización estilo Matlab. Para usarlo:
    
    from matplotlib.pyplot import 
    plot(tt, xx)
    Podés consultar en el foro cualquier duda o problema que tengas. Buena suerte!


"""

import numpy as np
import matplotlib.pyplot as plt
from math import *


def mi_funcion_sen(vmax = 1, dc = 0, freq= 1, phi = 0, N = 64, fs = 100):
    Vp = vmax #Volts
    wo = 2 * pi * freq #rads/s
    
    Ts = 1 / fs
    
    
    t = np.arange(0, N*Ts, Ts)
    f = Vp * (np.sin(wo * t + phi)) + dc
    
    return t,f

tt,ff = mi_funcion_sen(1, 5, 1, pi/4, 64, 100)
plt.figure()
plt.stem(tt,ff)
