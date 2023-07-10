from matplotlib.projections import polar
import numpy as np
import sympy as sym
import matplotlib.pyplot as plt

def Lagrange(xi,fi):
    '''
    This function is where Lagrange method occurs
    '''
    xi = np.array(xi)
    fi = np.array(fi)
    n = len(xi)
    x = sym.Symbol('x')
    pol = 0
    div = np.zeros(n, dtype = float)

    for i in range(0,n,1):
        numerator = 1
        denominator = 1
        for j  in range(0,n,1):
            if (j!=i):
                numerator *= (x-xi[j])
                denominador = denominator * (xi[i]-xi[j])
        Li = numerator/denominator

        pol = pol + Li*fi[i]
        div[i] = denominator

    psimple = pol.expand()
    px = sym.lambdify(x,psimple)
    samples = 101
    a = np.min(xi)
    b = np.max(xi)
    pxi = np.linspace(a,b,samples)
    pfi = px(pxi)
    return psimple,pxi,pfi

def defmatrix(n):
    '''
    This function creates an n * m Matrix
    '''
    matriz = []
    n = int(n)
    matrix = [float(input("Input data: ")) for i in range(n)] 
    return matrix

size = input("Input the size of the arrays: ")
print("Input your Xi data: (float) ")
xi = defmatrix(size)
print("Input your Yi data: (float) ")
fi = defmatrix(size)
psimple,pxi,pfi=Lagrange(xi,fi)
print("Polynomial: ", psimple)

# Make chart with plt
plt.plot(xi,fi,'o', label = 'Points')
plt.plot(pxi,pfi, label = 'Polynomial')
plt.legend()
plt.xlabel('xi')
plt.ylabel('fi')
plt.title(psimple)
plt.show()
