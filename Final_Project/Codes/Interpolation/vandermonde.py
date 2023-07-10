import numpy as np
import sympy as sym
import matplotlib.pyplot as plt

def vandermonde(xi,fi): 
    samples = 101
    xi = np.array(xi)
    B = np.array(fi)
    n = len(xi)

    #create vandermonde matrix
    A = np.zeros(shape=(n,n),dtype =float)
    for i in range(0,n,1):
        for j in range(0,n,1):
            power = (n-1)-j 
            A[i,j] = xi[i]**power

    coefficient = np.linalg.solve(A,B)  # Solve system
    x = sym.Symbol('x')
    polynomial = 0

    for i in range(0,n,1):
        power = (n-1)-i  
        term = coefficient[i]*(x**power)
        polynomial += term

    px = sym.lambdify(x,polynomial)

    a = np.min(xi)
    b = np.max(xi)
    xin = np.linspace(a,b,samples)
    yin = px(xin)
    return A, coefficient,polynomial, xin, yin

def defmatrix(n):
    matrix = []
    n = int(n)
    matrix = [float(input("Input data: ")) for i in range(n)] 
    return matrix

size = input("Input the size of the arrays: ")

print("Input Xi data : ")
xi = defmatrix(size)
print("Input Yi data: ")
fi = defmatrix(size)

(A,coefficient,polynomial, xin, yin)=vandermonde(xi,fi)

print('Vandermonde Matrix: ')
print(A)
print('Polynomial coefficients: ')
print(coefficient)
print('Interpolation polynomial: ')
print(polynomial)

# Make the graph using plt
plt.plot(xi,fi,'o', label='[xi,fi]')
plt.plot(xin,yin, label='p(x)')
plt.xlabel('xi')
plt.ylabel('fi')
plt.legend()
plt.title("Vandermonde")
plt.show()
