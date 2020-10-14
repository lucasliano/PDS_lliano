# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 02:23:21 2020

Este archivo permite verificar que la librería este funcionando correctamente

@author: LucasLiaño
"""
#%% Agrego librería propia al path
import sys
sys.path.append('D:/LucasLiaño/Escritorio/Lucas/UTN/PSD/Tareas (Spyder)')

#%%
import myLibrary as my

fs = 1000
N = 1000

t1,f1 = my.SignalGenerator ('sin',(100, 1) ,fs, N, (0, 0));
k1, Fk1, kk1, Fkk1 = my.DFT(f1, N, True);
