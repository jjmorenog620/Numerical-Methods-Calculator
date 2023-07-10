import numpy as np

def calculate(A,B):
    A = np.array(A,dtype=float) 
    B = np.array(B,dtype=float) 

    AB  = np.concatenate((A,B),axis=1)
    AB0 = np.copy(AB)

    size = np.shape(AB)
    n = size[0]
    m = size[1]

    for i in range(0,n-1,1):
        columna  = abs(AB[i:,i])
        dondemax = np.argmax(columna)
        
        if (dondemax !=0):
            temporal = np.copy(AB[i,:])
            AB[i,:] = AB[dondemax+i,:]
            AB[dondemax+i,:] = temporal
    AB1 = np.copy(AB)

    for i in range(0,n-1,1):
        pivote   = AB[i,i]
        adelante = i + 1
        for k in range(adelante,n,1):
            factor  = AB[k,i]/pivote
            AB[k,:] -= AB[i,:]*factor

    lastrow = n-1
    lastcolumn = m-1
    X = np.zeros(n,dtype=float)

    for i in range(lastrow,0-1,-1):
        summ = 0
        for j in range(i+1,lastcolumn,1):
            summ += AB[i,j]*X[j]
        b = AB[i,lastcolumn]
        X[i] = (b-summ)/AB[i,i]

    X = np.transpose([X])

    return (AB0, AB1, AB, X)

def defMatrixA(n):
    matrix = []
    n = int(n)
    print('Insert matrix A values: ')

    for i in range(n):
        matrix.append([])
        for j in range(n):
            val = float(input('Insert value: '))
            matrix[i].append(val)

    return matrix

def defMatrixB(n):
    matrix = []
    n = int(n)
    print('Insert matrix b values: ')

    for i in range(n):
        matrix.append([])
        for j in range(1):
            val = float(input('Insert value: '))
            matrix[i].append(val)

    return matrix

size = input("Insert matrix's size: ")

A = defMatrixA(size)
B = defMatrixB(size)

print('Matrix A:')
print(A)
print('Matrix B: ')
print(B)

(AB0, AB1, AB, X) = calculate(A,B)

print('Augmented matrix: ')
print(AB0)
print('Partial pivoting')
print(AB1)
print('Forward elimination')
print(AB)
print('Matrix X: ')
print(X)
print('Verification Ax=B: ')
print(np.dot(A,X))
