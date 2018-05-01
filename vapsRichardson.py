####Codi vapsRichardon.py per calcular els valors propis####

#Llibreries
import numpy as np
import sturm
import tridiagonal
import interpolacio
import potential

#Funcio vapsRichardon
#rmin,rmax.... Extrems d'abscisses
#ninterv...... Nombre intervals per tridiagonal
#n1, n2 ...... Posicio del vaps que es determinen
#error ....... Error absolut maxim tolerat
#Fitxer potencial.py conte la funcio potencial
def vapsRichardson(rmin,rmax,ninterv,n1,n2,error):
    class Error(Exception): pass
    try:
        #Constants i variables
        nintmax = 1000
        nnp = 48*ninterv
        nvalmax = 100
        d = np.zeros(nnp)
        hh = np.zeros(10)
        nval = n2 - n1 + 1
        valp = np.zeros(nval)
        val = np.zeros((10,nval))
        #Per a l'extrapolacio de Richardson
        nstep = np.array([1,2,3,4,6,8,12,16,24,48])
        #Comprovacio de dimensions maximes
        if (ninterv > nintmax):
            print('Massa intervals, nintmax = %d' % nintmax)
            raise Error
        if (nval > nvalmax):
            print('Massa val. propis, nvalmax = %d' % nvalmax)
            raise Error
        #Cicle d'extrapolacio
        for i in xrange(1,11):
            nnpunts = nstep[i-1]*ninterv
            h = (rmax - rmin)/nnpunts
            hh[i-1] = h**2
            n = nnpunts - 1
            for j in xrange(1,n+1):
                d[j-1] = potential.potential(rmin + j*h)
            val[i-1,:] = tridiagonal.tridiagonal(d,h,n,n1,n2)
            #Extrapolacio de Richardson
            errr = 0.0
            for l in xrange(1,nval+1):
                err = 0.0
                if (i == 1):
                    pass
                else:
                    valp[l-1],err = interpolacio.interpolacio(hh[0:i],val[0:i,l-1],i,0.0)
                    errr = max(errr,err)
                if ((i >= 2) and ((errr - error) < 1e-12)):
                    return valp
        print('No hem arribat al error')        
    except Error:
        print('Error a Richardson')
        
      
        
    
    
    
    
    
    
    
    
    
    
    