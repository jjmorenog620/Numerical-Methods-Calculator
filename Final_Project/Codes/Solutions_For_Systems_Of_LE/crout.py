import numpy as np

def matrixLU(matr):
    m = len(matr)
    matrix = np.zeros([m,m])
    U = np.zeros([m,m])
    L = np.zeros([m,m])

    matrix = np.array(matr,dtype=float) 
    U = np.array(matr,dtype=float)

    for k in range(0,m):
        for r in range(0,m):
            if (k == r):
                L[k,r] = 1
            if(k < r):
                factor = (matrix[r,k] / matrix[k,k])
                L[r,k] = factor
                for c in range(0,m):
                    matrix[r,c] = matrix[r,c] - (factor*matrix[k,c])
                    U[r,c] = matrix[r,c]
    return L, U

def forwardSubstitution(L, b):
    AB  = np.concatenate((L,b),axis=1)
    size = np.shape(AB)
    n = size[0]
    m = size[1]
    for i in range(0,n-1,1):
        pivot   = AB[i,i]
        forward = i + 1
        for k in range(forward,n,1):
            factor  = AB[k,i] / pivot
            AB[k,:] -=  AB[i,:]*factor
    return AB


def back_substitution(U, y):
    AB  = np.concatenate((U,y), axis = 1)
    size = np.shape(AB)
    n = size[0]
    m = size[1]
    lastrow = n-1
    lastcolumn = m-1
    X = np.zeros(n,dtype=float)

    for i in range(lastrow,0-1,-1):
        summ = 0
        for j in range(i + 1,n,1):
            summ = summ + AB[i,j]*X[j]
        b = AB[i,lastcolumn]
        X[i] = (b-summ) / AB[i,i]

    X = np.transpose([X])
    return X

def crout(A,b):
    A = np.array(A,dtype=float)
    b = np.array(b,dtype=float)

    L,U = matrixLU(A)
    z = forwardSubstitution(L,b)
    x = back_substitution(U,z)
    return L,U,x

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

    print('Insert matrix B values: ')
    for i in range(n):
        matrix.append([])
        for j in range(1):
            val = float(input('Insert value: '))
            matrix[i].append(val)

    return matrix

tam = input("Insert the matrix's size: ")

A = defMatrixA(tam)
B = defMatrixB(tam)

(L,U,X) = crout(A, B)
print('Matrix L')
print(L)
print('Matrix U')
print(U)
print('Solution')
print(X)
print('Verification Ax=B: ')
print(np.dot(A,X))
