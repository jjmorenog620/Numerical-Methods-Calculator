import numpy as np
import sympy as sym
import matplotlib.pyplot as plt

def linealplot(xi,fi):
    n = len(xi)
    x = sym.Symbol('x')
    px_tabla = []
    
    tr = 1
    while not(tr>=n):
        numerator = fi[tr]-fi[tr-1]
        denominator = xi[tr]-xi[tr-1]
        m = numerator/denominator
        pxtr = fi[tr-1] + m*(x-xi[tr-1])
        px_tabla.append(pxtr)
        tr = tr + 1
        
    return(px_tabla)

def defmatrix(n):
    matrix = []
    n = int(n)
    matrix = [float(input("Input data: ")) for i in range(n)] 
    return matrix

size = input("Input the size of the arrays: ")
print("Input your Xi data: ")
xi = defmatrix(size)
print("Input your Yi data: ")
fi = defmatrix(size)
samples = int(input("Input the size of the arrays: "))
n = len(xi)
px_tabla = linealplot(xi,fi)

print('Piecewise polynomial ')
for tr in range(1,n,1):
    print('  x = ['+str(xi[tr-1])
          +','+str(xi[tr])+']')
    print(str(px_tabla[tr-1]))

xtrz = np.array([])
ytrz = np.array([])
tr = 1
while not(tr>=n):
    a = xi[tr-1]
    b = xi[tr]
    xtr = np.linspace(a,b,samples)
    pxtr = px_tabla[tr-1]
    pxt = sym.lambdify('x',pxtr)
    ytr = pxt(xtr)
    # vectors for x , y
    xtrz = np.concatenate((xtrz,xtr))
    ytrz = np.concatenate((ytrz,ytr))
    tr = tr + 1

# Make the graph
plt.plot(xi,fi,'o', label='points')
plt.plot(xtrz,ytrz, label='plotter')
plt.title('Lineal Plot (splines)')
plt.xlabel('xi')
plt.ylabel('px(xi)')
plt.legend()
plt.show()
