# Import numpy and plt
import numpy as np
import matplotlib.pyplot as plt

def Interpolation(xi,fi):
    ''' 
    This function is where interpolation happens
    '''
    xi = np.array(xi) # Initial X
    fi = np.array(fi) 
    lenghtOfXi = len(xi)
    A=np.zeros((lenghtOfXi,lenghtOfXi)) # create a new array of given shape and fill with zero values
    for i in range(lenghtOfXi):
        A.T[i] = xi**i
    a=np.linalg.solve(A,fi)

    xteor = np.linspace(min(xi),max(xi),100)
    yteor = 0
    for i in range(lenghtOfXi):
        yteor = yteor + a[i] * xteor **i
    board=[[], []]
    for i in range(len(xteor)):
        board[0].append(xteor[i])
        board[1].append(yteor[i])
    return board

def defmatrix(n):
    ''' 
    This function creates an n * m matrix
    '''
    matrix = []
    n = int(n)
    matrix = [float(input('Input your data: ')) for i in range(n)] 
    return matrix

size = input("Input the size of the arrays: ")

print("Input your Xi data: ")
xi = defmatrix(size)
print("Input your Yi data: ")
fi = defmatrix(size)

board = Interpolation(xi,fi)

print("Xi\t\t\tYi")
for i in range(len(board[0])):
    print(board[0][i],"\t",board[1][i])

# Make chart with plt

plt.plot(xi,fi,'ro')
plt.plot(board[0],board[1],'b-')
plt.legend()
plt.xlabel('X')
plt.ylabel('Y')
plt.title("Interpolation")
plt.show()
