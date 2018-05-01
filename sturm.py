####Codi sturm.py per calcular NC de valors propis####

#Llibreries
import numpy as np

#Funcio sturm
#d(1...N)..... Valors de la diagonal
#e2........... Valors supradiagonals al quadrat
#n............ Dimensio de la matriu
#x............ Valor d'abcisses pel # de valors propis
def sturm(d,e2,n,x):
    skip = False
    nc = 0
    q = d[0] - x
    if (abs(q) < 1e-12): skip = True
    if (q <= 1e-12): nc = 1
        
    for i in xrange(2,n+1):
        if (skip):
            skip = False
            continue
        if (abs(q) > 1e-12):
            q = d[i-1] - x - e2/q
            if (abs(q) < 1e-12):
                skip = True
        else:
            q = d[i-1] - x
            if (abs(q) < 1e-12):
                skip = True
        if (q <= 1e-12): nc = nc + 1
    return nc
