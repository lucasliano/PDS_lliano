# -*- coding: utf-8 -*-
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
    
    
    
    
    return tfinal, ffinal, ns