####Codi interpolacio.py per calcular NC de valors propis####

#Llibreries
import numpy as np

#Funcio interpolacio
#x(a)......... Punts d'abscisses
#y(a)......... Punts d'abscisses
#n............ Nombre de punts
#x............ Punt on evaluem l'interpolacio
def interpolacio(xa,ya,n,x):
    class Error(Exception): pass
    try:
        nmax = 20
        d = np.zeros((nmax,2))
        if (n > nmax):
            print('n = %d, hauria de ser menor de 20' % n)
            raise Error
        for i in xrange(1,n+1):
            d[i-1,0] = ya[i-1]
        inn = 0
        ioo = 1
        for j in xrange(1,n):
            for i in xrange(1,n-j+1):
                den = xa[i+j-1] - xa[i-1]
                if (abs(den) < 1e-12):
                    print('Dues abscisses iguals')
                    raise Error
                d[i-1,ioo] = ((x - xa[i-1])*d[i,inn] - (x - xa[i+j-1])*d[i-1,inn])/den
            ixx = inn
            inn = ioo
            ioo = ixx
        y = d[0,inn]
        error = max(abs(y - d[0,ioo]), abs(y - d[1,ioo]))   
    except Error:
        print('Error a interpolacio')
    return y, error
