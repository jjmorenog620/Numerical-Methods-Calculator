import numpy as np

def Gauss_Seidel(A,B,X0,tolera,iteramax):
  A = np.array(A,dtype=float) 
  B = np.array(B,dtype=float)
  size = np.shape(A)
  n = size[0]
  m = size[1]
  X = np.copy(X0)
  diferencia = np.ones(n, dtype=float)
  error = 2*tolera

  itera = 0
  while not(error<=tolera or itera>iteramax):
      for i in range(0,n,1):
          summ = 0 
          for j in range(0,m,1):
              if (i!=j): 
                  summ = summ - A[i,j]*X[j]
          
          nuevo = (B[i]+summ) / A[i,i]
          diferencia[i] = np.abs(nuevo-X[i])
          X[i] = nuevo
      error = np.max(diferencia)
      itera = itera + 1

  X = np.transpose([X])

  if (itera>iteramax):
      X=0

  verify = np.dot(A,X)

  return X, verify

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
    
    for i in range(n):
        matrix.append([])
        for j in range(1):
            val = float(input('Insert value: '))
            matrix[i].append(val)

    return matrix

size = input("Insert matrix's size: ")

A = defMatrixA(size)
print('Insert matrix B values: ')
B = defMatrixB(size)
print('Insert matrix x0 values: ')
X0 = defMatrixB(size)
tolera = float(input('Insert tolerance: '))
iteramax = int(input('Insert number of iterations: '))
(X, verify) = Gauss_Seidel(A,B,X0,tolera,iteramax)

print('Matrix A:')
print(A)
print('Matrix B: ')
print(B)
print('Outcome X: ')
print(X)
print('Verify Ax=B: ')
print(verify)
