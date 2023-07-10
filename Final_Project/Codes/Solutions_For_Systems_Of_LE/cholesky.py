from math import sqrt
from sys import exit
import numpy as np

def ifSymmetricMatrix(A):
	#Checking if A is symmetric

	for i in range(len(A)):
		for j in range(i + 1,len(A)):
			if A[i][j] != A[j][i]:
				return False
	return True 


def cholesky(A):
	#Cholesky method

	if not ifSymmetricMatrix(A):
		exit('Matrix is asymmetric')
	n = len(A)
	G = [[0.0]*n for j in range(n)]
	for i in range(n):
		summ = A[i][i]
		for k in range(i):
			summ -= A[k][i]**2
		if summ < 0:
			exit('Matrix is not positive definite')	
		A[i][i] = sqrt(summ)
		for j in range(i + 1, n):
			summ = A[i][j]
			for k in range(i):
				summ -= A[k][i] * A[k][j]
			A[i][j] = summ / A[i][i]

	for j in range(n):
		for i in range(n):
			if(i > j):
				A[i][j] = 0.0

	return np.array(A)


def defMatrix(n):
	#Creates the matrix to apply cholesky on

    matrix = []
    n = int(n)

    for i in range(n):
        matrix.append([])
        for j in range(n):
            val = int(input('Insert value: '))
            matrix[i].append(val)

    return matrix

matr = defMatrix(input("Insert the matrix's size: "))

print('Matrix A')
print(np.array(matr))
outcome = cholesky(matr)
outcomet = outcome.transpose()
print('Matrix L')
print(outcomet)
print('Matrix L Transpose')
print(outcome)
print('L*LT: ')
print(np.dot(outcomet,outcome))
