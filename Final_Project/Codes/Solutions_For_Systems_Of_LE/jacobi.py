import numpy as np

def jacobi(A,B,mi):
    A = np.array(A,dtype=float) 
    B = np.array(B,dtype=float)
    x=[0.0]*len(B)
    count=0
    while(count<mi):
        for i in range(0,len(A)):
            sigma=0.0
            for j in range(0,len(A)):
                if(i!=j):
                    sigma += (A[i,j]*x[j])
                    x[i] = float((B[i] - sigma)/A[i,i])
        count +=1
    print('Iterations: ',count)
    return x

def defMatrixA(n):
    matriz = []
    n = int(n)
    print('Insert matrix A values: ')

    for i in range(n):
        matriz.append([])
        for j in range(n):
            val = float(input('Insert value: '))
            matriz[i].append(val)

    return matriz

def defMatrixB(n):
    matriz = []
    n = int(n)
    print('Insert matrix B values: ')

    for i in range(n):
        matriz.append([])
        for j in range(1):
            val = float(input('Insert value: '))
            matriz[i].append(val)

    return matriz

size = input("Insert matrix's size: ")

A = defMatrixA(size)
B = defMatrixB(size)
ite = int(input('Number of iterations: '))

resu=jacobi(A,B,ite)

print('Matrix A: ')
print(A)
print('Matrix B')
print(B)
print('Matrix X: ', resu)
print('Verification Ax=B: ', np.dot(A,resu))
