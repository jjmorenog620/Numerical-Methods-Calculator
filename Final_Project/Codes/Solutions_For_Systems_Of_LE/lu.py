import numpy as np

def matrixLU(mat):
    m = len(mat)
    matrix=np.zeros([m,m])
    U=np.zeros([m,m])
    L=np.zeros([m,m])

    matrix=np.array(mat,dtype=float) 
    U=np.array(mat,dtype=float)

    for k in range(0,m):
        for r in range(0,m):
            if (k==r):
                L[k,r] = 1
            if(k<r):
                factor = (matrix[r,k]/matrix[k,k])
                L[r,k] = factor
                for c in range(0,m):
                    matrix[r,c] = matrix[r,c] - (factor*matrix[k,c])
                    U[r,c] = matrix[r,c]
    return L,U

def defMatrix(n):
    matrix = []
    n = int(n)
    print("Insert matrix values: ")

    for i in range(n):
        matrix.append([])
        for j in range(n):
            val = int(input("Insert value: "))
            matrix[i].append(val)

    return matrix

mat = defMatrix(input("Insert matrix's size: "))



(L,U) = matrixLU(mat)
print("Matrix given: ")
print(mat)
print("Outcomes: \n")
print("Matrix L")
print(L)
print("Matrix U")
print(U)
print("LU Verification: ")
print(np.dot(L,U))
