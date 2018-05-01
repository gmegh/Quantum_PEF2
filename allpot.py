####Codi potential.py per calcular NC de valors propis####

#Llibreries
import numpy as np

#Funcio potential
#x............ Valor d'abcisses on s'evalua potencial
def potential(x):
     V[i-1] = (rmin + k*h)**2   
     V[i-1] = 5*((rmin + h*i)**2 -1)**2  # plt.ylim((0, 20)) plt.xlim((-4, 4))
     V[i-1] = (rmin + h*i)**4
     V[k-1] = -17/((np.cosh(rmin + k*h))**2) # rmin = -4, rmax = 4, plt.ylim((-17.5, 2.5)) plt.xlim((-4, 4))
     
        # Condensador, rmin = -1, rmax = 6, plt.ylim((-1, 30)), xlim no posis re
     
    for k in range(1,int(n/10)+1):
        V[k-1] = 500

    for k in range(int(n/10)+1,int(9*n/10)+1):
        V[k-1] = 3*k*h

    for k in range(int(9*n/10)+1,n+1):
        V[k-1] = 500   
    
    # Lennard Jones, Rmin = 0, Rmax = 20, plt.ylim((-10,0)) i xlim res
    for k in range(1,n+1):
        V[k-1] = 40*((8/(rmin + k*h) )**12-(8/(rmin + k*h ))**6)

    
    
    return V
