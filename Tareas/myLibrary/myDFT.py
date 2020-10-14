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
    
    Fkk = Fk[:int(N/2)] * (1/N) # Recortamos la señal hasta fs/2 y la escalamos en (2/N)
    kk = k[:int(N/2)]          # También recortamos la base temporal
    
    if (escala = 'a'): # Si queremos que coincida la amplitud 
        Fkk = Fkk * 2
    elif (escala = 'p'): # Si queremos que coincida la potencia en tiempo con la pot en w
        Fkk = Fkk * np.sqrt(2)
    
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