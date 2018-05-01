####Codi trapezoidal.py####

#Llibreries
import numpy as np

#Funcio trapezoidal per la posicio mitjana
#f(1...N)..... Valors de la funcio
#h............ Pas de discretitzacio
def trapezoidal(f,x,h):
    
    n = len(f)
    x_mean = 0.5*f[0]*x[0] + 0.5*f[n-1]*x[n-1]
    for i in xrange(2,n):
        x_mean = x_mean + f[i-1]*x[i-1]
    x_mean = x_mean*h
    return x_mean
        
      
        
    
    
    
    
    
    
    
    
    
    
    