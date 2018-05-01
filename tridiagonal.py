####Codi tridiagonal.py per calcular els valors propis####

#Llibreries
import numpy as np
import sturm

#Funcio tridiagonal
#d(1...N)..... Valors de potencial que sera la diagonal
#h............ Pas de discretitzacio
#n............ Dimensio de la matriu
#n1, n2 ...... Posicio del vaps que es determinen
def tridiagonal(d,h,n,n1,n2):
    #Constants i variables
    eps = 1e-12
    maxiter = 200
    lmax = False
    lmin = False
    w = np.zeros(n2-n1+1)
    
    #Parametres
    e = 1/h**2
    e2 = e**2
    dosdivh2 = 2/h**2
    xmin = d[0]
    for i in xrange(1,n+1):
        xmin = min(xmin,d[i-1])
        d[i-1] = d[i-1] + dosdivh2
    #Calculem fita superior
    xl = e + max(abs(d[0]),abs(d[n-1]))
    for i in xrange(2,n+1):
        xl = max(xl,(abs(d[i-1])+2*e))
    xmax = xl
    #Algoritme de biseccio comencat al vap n1
    ivp = 0
    if (n1 < 1): n1 = 1
    if (n2 > n): n2 = n
        
    class NoConv(Exception): pass
    
    try:
        for i in xrange(n1,n2+1):
            for itr in xrange(1,maxiter+1):
                lmax = False
                x = (xmax + xmin)/2
                nc = sturm.sturm(d,e2,n,x)
                if (nc >= n2): xl = min(xl,x)
                #Es fita superior?
                if (nc >= i): xmax = x
                if (nc == i): lmax = True
                #Es fita inferior?
                if (nc < i): xmin = x
                if (nc == i-1): lmin = True
                if (lmin and lmax): break
                if (itr == maxiter): raise NoConv
            #Valors propi i fitat
            a = xmin
            b = xmax
            #Biseccio
            for it in xrange(1,57):
                x = (b + a)/2
                if ((abs(x-a) < 1e-12) or ((b-a) <= (eps*(xmax-xmin)))):
                    break
                nc = sturm.sturm(d,e2,n,x)
                if (nc == i):
                    b = x
                else:
                    a = x
            w[ivp] = (b + a)/2
            ivp = ivp + 1
            xmin = xmax
            xmax = xl
        #Recuperem el potencial
        for k in xrange(1,n+1):
            d[k-1] = d[k-1] - dosdivh2
    except NoConv:
        print('No convergeix tridiagonal')
    return w
        
      
        
    
    
    
    
    
    
    
    
    
    
    