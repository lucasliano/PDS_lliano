# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 02:15:27 2020

    Este es un Dummy File para poder crear la librería

@author: LucasLiaño
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as signal


#__all__ = ["myDFT", "mySignalGenerator"]

#%% Se crea la función ADC

"""
Created on Sat Oct  3 12:02:39 2020

Resumen:

    fsampled, ns = ADC(f, t, fs = 2000, bits = 8, PositiveVref = 5, NegativeVref = 0)

    La función toma la secuencia f, que supone una señal continua de frecuencia de muestro fs1,
    y la ingresa al sistema simulando el paso por un ADC. 
    De esta manera los campos que pueden ser modificados son las tensiones a las cuales está
    expuesta el ADC y la cantidad de bits del mismo. 
    
    De esta forma el ADC por defecto tiene 8 bits, es decir 256 palabras, entre las tensiones 0v y +5v
    
    La función devuelve los valores de la señal sampleada y la distribución del ruido de cuantización en func del tiempo.
@author: LucasLiaño
"""

def ADC (f, t, fs = 2000, bits = 8, PositiveVref = 5, NegativeVref = 0):
    Tsi = t[1] - t[0]
    step = int( (1/fs) / Tsi )     # Si fsi = 1kHz => step = 2
    
    q = (PositiveVref - NegativeVref) / (2**bits)  # Volts por muestra
    #ybins = np.arange(NegativeVref, PositiveVref,q)
    
    fo = np.zeros(int( np.floor(np.size(f)/step) ))    # Si f tiene 1000 muestras, fo tiene 500 con step 2
    index = 0
    for each in f[::step]:
        fo[index] = each
        index = index + 1
    
    tfinal = np.zeros(int(np.floor(np.size(t)/step) ))    # Si f tiene 1000 muestras, fo tiene 500 con step 2
    index = 0
    for each in t[::step]:
        tfinal[index] = each
        index = index + 1
    
    
    
    fclip = np.zeros(np.size(fo))
    index = 0
    for each in fo:
        if each < NegativeVref:
            fclip[index] = NegativeVref
        elif each > PositiveVref:
            fclip[index] = PositiveVref
        else:
            fclip[index] = fo[index]
        index = index + 1
    
            
            
    fnorm = fclip * (1/q)       # Lo llevamos al dominio de las muestras en Y
    
    fsampled = np.rint(fnorm)   # Redondeamos
    
    ns = fnorm - fsampled       # Calculamos en el dominio de las muestras el ruido de quant.
   
    nsfinal = ns * q            # Volvemos a llevarlo al dominio de los volts
    
    ffinal = fsampled * q       # Volvemos a llevarlo al dominio de volts en Y
    

    fig = plt.figure(1)
    ax = fig.add_subplot(1, 1, 1)
    ax.hist(ns)
    ax.set_xlabel('Valor redondeado')  
    ax.set_ylabel('Ocurrencias')  
    ax.set_title("Histograma del ruido de cuantización") 
    
    fig, axs = plt.subplots(2,1,True,True)
    axs[0].grid()
    axs[1].grid()    
                  
    axs[0].plot(t,f) 
    #axs[0].set_xlabel('Tiempo [nTs]')  
    axs[0].set_ylabel('Amplitud [V]')  
    axs[0].set_title("Señal original") 
                  
    axs[1].plot(tfinal,ffinal, color = 'g')
    axs[1].set_xlabel('Tiempo [nTs]')  
    axs[1].set_ylabel('Amplitud [V]')  
    axs[1].set_title("Señal muestreada con q = " + str(q) + " V/div entre " + str(NegativeVref) + "v y " + str(PositiveVref) +"v") 
    
    
    
    
    return tfinal, ffinal, nsfinal


#%% Se crea la función DFT
"""
Created on Wed Sep 16 01:58:21 2020

Resumen:

    k, Fk, kk, Fkk = DFT(f, N, plotting = False, nombre = 'f(t)', colorTrazo = 'b', escala='a')
    
    La función devuelve la transformada discreta de Fourier completa (k, Fk)
    y las tranformadas recortadas entre 0 y fs/2 y escaladas. 
    
    Si plotting = True, imprime un gráfico cool :D

@author: LucasLiaño
"""


def DFT(f, N, W=1, plotting = False, nombre='f(t)', colorTrazo = 'b', escala='a'):
    
    k = np.arange(0,N).astype(int)      #Calculamos la base temporal discreta

    Fk = np.zeros(N).astype(complex)    #Generamos un vector vacio con la salida
    
    Wkn = np.zeros([k.size,k.size], dtype = complex)    #k va de 0 a N-1 y n lo mismo
   
    index = 0
    for kloop in k:
        Wkn[:,kloop] = np.exp( -1j * (2*np.pi/N) * kloop * k)
        index += 1
    
    Fk = np.matmul(Wkn,f)
    
    Fkk = Fk[:int(N/2)] * (1/N) # Recortamos la señal hasta fs/2 y la escalamos en (1/N)
    kk = k[:int(N/2)]          # También recortamos la base temporal
    
    if (escala == 'a'): # Si queremos que coincida la amplitud 
        Fkk = Fkk * 2
    elif (escala == 'p'): # Si queremos que coincida la potencia en tiempo con la pot en w
        Fkk = Fkk * np.sqrt(2)
    elif (escala == 'n'): # Sin escala
        Fkk = Fkk * 1
    
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
        
        # axs[1,0].plot(kk*W, np.real(Fkk), label = nombre, color= colorTrazo)  
        # axs[1,0].set_xlabel('Frecuencia [k*W]')  
        # axs[1,0].set_ylabel('Amplitud [V]')  
        # axs[1,0].set_title("Parte Real") 
        # axs[1,0].legend()
        
                      
        # axs[1,1].plot(kk*W, np.imag(Fkk), label = nombre, color= colorTrazo)  
        # axs[1,1].set_xlabel('Frecuencia [k*W]')  
        # axs[1,1].set_ylabel('Amplitud [V]')  
        # axs[1,1].set_title("Parte Imaginaria") 
        # axs[1,1].legend()
    
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
    if np.size(t) != N:
        t = t[:N]
    
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
        
#%% Creo función para graficar en dB

def to_db(f):
    fdb = 20 * np.log10(f)
    return fdb