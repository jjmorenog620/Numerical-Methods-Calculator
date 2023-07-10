import numpy as np
import sympy as sym
import matplotlib.pyplot as plt

def divided_differences(xi,fi):
    xi = np.array(xi,dtype=float)
    fi = np.array(fi,dtype=float)
    title = ['i   ','xi  ','fi  ']
    n = len(xi)
    ki = np.arange(0,n,1)
    board = np.concatenate(([ki],[xi],[fi]),axis=0)
    board = np.transpose(board)
    dfinite = np.zeros(shape=(n,n),dtype=float)
    board = np.concatenate((board,dfinite), axis=1)

    # calculate board
    [n,m] = np.shape(board)
    diagonal = n-1
    j = 3

    while (j < m):
        # add title
        title.append('F['+str(j-2)+']')

        i = 0
        step = j-2 # start in 1
        while (i < diagonal):
            denominator = (xi[i+step]-xi[i])
            numerator = board[i+1,j-1]-board[i,j-1]
            board[i,j] = numerator/denominator
            i = i+1
        diagonal = diagonal - 1
        j = j+1

    dDivid = board[0,3:]
    n = len(dfinite)

    # expresión del polinomio con Sympy
    x = sym.Symbol('x')
    polynomial = fi[0]
    for j in range(1,n,1):
        factor = dDivid[j-1]
        term = 1
        for k in range(0,j,1):
            term *= (x-xi[k])
        polynomial = polynomial + term*factor

    # simplify (x-xi)
    polisimple = polynomial.expand()

    # numerical eval
    px = sym.lambdify(x,polisimple)

    # points
    samples = 101
    a = np.min(xi)
    b = np.max(xi)
    pxi = np.linspace(a,b,samples)
    pfi = px(pxi)

    return polisimple, pxi, pfi


def defmatrix(n):
    matrix = []
    n = int(n)
    matrix = [float(input("input data: ")) for i in range(n)] 
    return matrix

size = input("Input the size of the arrays: ")
print("Input Xi data : ")
xi = defmatrix(size)
print("Input Yi data: ")
fi = defmatrix(size)

polynomial,pxi,pfi=divided_differences(xi,fi)
print("Polynomial: ", polynomial)

# Graph
plt.plot(xi,fi,'o', label = 'Points')
plt.plot(pxi,pfi, label = 'Polynomial')
plt.legend()
plt.xlabel('xi')
plt.ylabel('fi')
plt.title(polynomial)
plt.show()
