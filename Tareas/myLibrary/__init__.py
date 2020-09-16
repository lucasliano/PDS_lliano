# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 02:15:27 2020

    Este es un Dummy File para poder crear la librería

@author: LucasLiaño
"""

import numpy as np
import matplotlib.pyplot as plt


#__all__ = ["myDFT", "mySignalGenerator"]

"""
Created on Wed Sep 16 01:58:21 2020

Resumen:

    k, Fk, kk, Fkk = DFT(f, N, plotting = False, nombre = 'f(t)', colorTrazo = 'b')
    
    La función devuelve la transformada discreta de Fourier completa (k, Fk)
    y las tranformadas recortadas entre 0 y fs/2 y escaladas. 
    
    Si plotting = True, imprime un gráfico cool :D

@author: LucasLiaño
"""

#%% Se crea la función DFT
def DFT(f, N, plotting = False, nombre='f(t)', colorTrazo = 'b'):
    W = 1/((f[1]-f[0])*N)
    
    k = np.arange(0,N).astype(int)      #Calculamos la base temporal discreta

    Fk = np.zeros(N).astype(complex)    #Generamos un vector vacio con la salida
    
    Wkn = np.zeros([k.size,k.size], dtype = complex)    #k va de 0 a N-1 y n lo mismo
   
    index = 0
    for kloop in k:
        Wkn[:,kloop] = np.exp( -1j * (2*np.pi/N) * kloop * k)
        index += 1
    
    Fk = np.matmul(Wkn,f)
    
    Fkk = Fk[:int(N/2)] * (2/N) # Recortamos la señal hasta fs/2 y la escalamos en (2/N)
    kk = k[:int(N/2)]          # También recortamos la base temporal
    
    if plotting == True:
        
        fig, axs = plt.subplots(2,2)
                      
        axs[0,0].plot(kk*W, np.abs(Fkk), label = nombre, color= colorTrazo)  
        axs[0,0].set_xlabel('Frecuencia [k*W]')  
        axs[0,0].set_ylabel('Amplitud [V]')  
        axs[0,0].set_title("Módulo") 
        axs[0,0].legend()
                      
        axs[0,1].plot(kk*W, np.angle(Fkk), label = nombre, color= colorTrazo)  
        axs[0,1].set_xlabel('Frecuencia [k*W]')  
        axs[0,1].set_ylabel('Amplitud [V]')  
        axs[0,1].set_title("Fase") 
        axs[0,1].legend()
        
        axs[1,0].plot(kk*W, np.real(Fkk), label = nombre, color= colorTrazo)  
        axs[1,0].set_xlabel('Frecuencia [k*W]')  
        axs[1,0].set_ylabel('Amplitud [V]')  
        axs[1,0].set_title("Parte Real") 
        axs[1,0].legend()
        
                      
        axs[1,1].plot(kk*W, np.imag(Fkk), label = nombre, color= colorTrazo)  
        axs[1,1].set_xlabel('Frecuencia [k*W]')  
        axs[1,1].set_ylabel('Amplitud [V]')  
        axs[1,1].set_title("Parte Imaginaria") 
        axs[1,1].legend()
    
    return k, Fk, kk, Fkk

#%% SignalGenerator
"""
Created on Wed Sep 16 02:24:04 2020

Resumen:
        
          t, f = SignalGenerator (sType ='sin',param =(1, 1) ,fs = 1000, N = 1000, optionalParam=(0, 0)):

    Esta función retorna una función con base temportal t.

@author: LucasLiaño
"""
def SignalGenerator (sType ='sin',param =(1, 1) ,fs = 1000, N = 1000, optionalParam=(0, 0)):
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
        
