####Codi wavefunction.py per calcular els valors propis####

#Llibreries
import numpy as np

#Funcio wavefunction
#d ........... Valors de potencial
#h ........... Pas de discretitzacio
#n ........... Dimensio de la matriu
#vp .......... Valor propi determinat

def wavefunction(d,h,n,vp):
    #Constants i variables
    wf = np.zeros(n)
    h2 = h*h
    #Recalculem la diagonal
    for k in xrange(1,n+1):
        d[k-1] = (d[k-1] - vp)*h2 + 2
    #Ajust per arrodoniments intolerables
    #Punt de trobada de la integracio
    nmed = n/2 + 2
    #Integracio d'esquerra a dreta
    wf[0] = 1.0
    wf[1] = d[0]
    norsum = 1 + d[0]**2
    for k in xrange(3,nmed+1):
        wf[k-1] = d[k-2]*wf[k-2] - wf[k-3]
        norsum = norsum + wf[k-1]**2
        #Preveu overflows: aplica reescalament
        if (abs(wf[k-1]) >= 1e15):
            for i in xrange(1,k+1):
                wf[i-1] = wf[i-1]/1e15
                norsum = norsum/1e30
    #Evita overflows en el factor d'igualacio
    if (abs(wf[nmed-1]) < 1e-12): nmed = nmed - 1
    #Integracio de dreta a esquerra
    wf[n-1] = 1.0
    wf[n-2] = d[n-1]
    for k in xrange(n-2,nmed,-1):
        wf[k-1] = d[k]*wf[k] - wf[k+1]
        if (abs(wf[k-1]) >= 1e15):
            for i in xrange(n,k-1,-1):
                wf[i-1] = wf[i-1]/1e15
    #Igualar dos trossos (calculem wf[nmed] amb wf[nmed+1] i wf[nmed + 2])
    wwf = d[nmed]*wf[nmed] - wf[nmed+1]
    #Factor d'igualacio
    fac = wf[nmed-1]/wwf
    #Reconstruim el interval de dalt i completem normalitzacio
    for k in xrange(nmed+1,n+1):
        wf[k-1] = wf[k-1]*fac
        norsum = norsum + wf[k-1]**2
    #Normalitzacio de les funcions d'ona (trapezoidal)
    xnorm = np.sqrt(1.0/(h*norsum))
    for k in xrange(1,n+1):
        wf[k-1] = xnorm*wf[k-1]
    #Recompondre la diagonal
    h2=h*h
    for k in xrange(1,n+1):
        d[k-1] = vp + (d[k-1] - 2)/h2
    return wf
    
    
      
              
   
                
    
    
    
    
        
      
        
    
    
    
    
    
    
    
    
    
    
    