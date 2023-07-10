import numpy as np
import sympy as sym
import matplotlib.pyplot as plt

def spline_natural(xi,yi):
    n = len(xi)
    # h values
    h = np.zeros(n-1, dtype = float)
    for j in range(0,n-1,1):
        h[j] = xi[j+1] - xi[j]

    A = np.zeros(shape=(n-2,n-2), dtype = float) #Create system of Equations
    B = np.zeros(n-2, dtype = float)
    S = np.zeros(n, dtype = float)
    A[0,0] = 2*(h[0]+h[1])
    A[0,1] = h[1]
    B[0] = 6*((yi[2]-yi[1])/h[1] - (yi[1]-yi[0])/h[0])

    for i in range(1,n-3,1):
        A[i,i-1] = h[i]
        A[i,i] = 2*(h[i]+h[i+1])
        A[i,i+1] = h[i+1]
        fac21 = (yi[i+2]-yi[i+1])/h[i+1]
        fac10 = (yi[i+1]-yi[i])/h[i]
        B[i] = 6*(fac21 - fac10)

    A[n-3,n-4] = h[n-3]
    A[n-3,n-3] = 2*(h[n-3]+h[n-2])
    fac12 = (yi[n-1]-yi[n-2])/h[n-2]
    fac23 = (yi[n-2]-yi[n-3])/h[n-3]
    B[n-3] = 6*(fac12 - fac23)
    r = np.linalg.solve(A,B) # Solve System

    for j in range(1,n-1,1):
        S[j] = r[j-1]
    S[0] = 0
    S[n-1] = 0
    a = np.zeros(n-1, dtype = float)
    b = np.zeros(n-1, dtype = float)
    c = np.zeros(n-1, dtype = float)
    d = np.zeros(n-1, dtype = float)

    for j in range(0,n-1,1):
        a[j] = (S[j+1]-S[j])/(6*h[j])
        b[j] = S[j]/2
        fac10 = (yi[j+1]-yi[j])/h[j]
        c[j] = fac10 - (2*h[j]*S[j]+h[j]*S[j+1])/6
        d[j] = yi[j]
    x = sym.Symbol('x')
    board = []

    for j in range(0,n-1,1):

        pxtr = a[j]*(x-xi[j])**3 + b[j]*(x-xi[j])**2
        pxtr = pxtr + c[j]*(x-xi[j])+ d[j]
        pxtr = pxtr.expand()
        px_tabla.append(pxtr)
    return(px_tabla)

def defmatrix(n):
    '''
    This functions creates a Matrix n*m
    '''
    matrix = []
    n = int(n)
    matrix = [float(input("Input data : ")) for i in range(n)] 
    return matrix

size = input("Input the size of the arrays : ")

print("Input your Xi data: ")
xi = defmatrix(size)
print("Input your Yi data : ")
fi = defmatrix(size)

samples = int(input("Input the size of the arrays: "))

n = len(xi)
board = spline_natural(xi,fi)

print('Piecewise polynomial')
for tr in range(1,n,1):
    print(' x = ['+str(xi[tr-1])
          +','+str(xi[tr])+']')
    print(str(board[tr-1]))

xtrz = np.array([])
ytrz = np.array([])
tr = 1
while not(tr>=n):
    a = xi[tr-1]
    b = xi[tr]
    xtr = np.linspace(a,b,samples)
    
    # eval polinomial
    pxtr = board[tr-1]
    pxt = sym.lambdify('x',pxtr)
    ytr = pxt(xtr)

    # vectors for x and y
    xtrz = np.concatenate((xtrz,xtr))
    ytrz = np.concatenate((ytrz,ytr))
    tr = tr + 1

# Make the graph
plt.plot(xi,fi,'ro', label='Points')
plt.plot(xtrz,ytrz, label='Plotter'
         , color='green')
plt.title('Spline Natural1')
plt.xlabel('xi')
plt.ylabel('px(xi)')
plt.legend()
plt.show()
