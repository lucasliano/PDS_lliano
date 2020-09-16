# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 02:24:04 2020

Resumen:
        
          t, f = mySignalGenerator (sType ='sin',param =(1, 1) ,fs = 1000, N = 1000, optionalParam=(0, 0)):

    Esta función retorna una función con base temportal t.

@author: LucasLiaño
"""

def mySignalGenerator (sType ='sin',param =(1, 1) ,fs = 1000, N = 1000, optionalParam=(0, 0)):
    Ts = 1/fs
    t = np.arange(0, N*Ts, Ts)
    
    if sType == 'sin':
        # Senoidal (fo=1, Ao=1)
        # optionalParam (phi=0, dc=0)
        #print("Senoidal")
        fo = param[0]
        Ao = param[1]
        phi = optionalParam[0]
        dc = optionalParam[1]
        
        f = Ao * (np.sin(2 * np.pi * fo * t + phi)) + dc
        return t,f
        
    elif sType == 'n':
        # Ruido blanco (u,std)
        # optionalParam (none,none)
        #print("White Noise")
        u = param[0]
        std = param[1]
        f = np.random.normal(u, std, size=N)
        return t, f
        
        
    elif sType == 't':
        # Triangular (To, Ao)
        # optionalParam (none,none)
        #print("Triangular")
        To = param[0]
        Ao = param[1]
        f = Ao/2 * signal.sawtooth(2 * np.pi * 1/To * t) + Ao/2
        return t, f
        
    elif sType == 'sq':
        # Cuadrada (To, Ao)
        # optionalParam = (none, none)
        #print("Square")
        To = param[0]
        Ao = param[1]
        f = Ao/2 * signal.square(2 * np.pi * 1/To *t) + Ao/2
        
        
        return t, f
    
    else:
        raise ValueError("El argumento sType debe ser 'sin','n','t' o 'sq'.")
        
