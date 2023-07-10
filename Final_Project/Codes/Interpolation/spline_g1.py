import numpy as np
import sympy as sym
import matplotlib.pyplot as plt

def lineal_interpolation(xi_values, fi_values):
    """
    Perform linear interpolation using the given xi and fi values.

    Args:
        xi_values (list): List of xi values.
        fi_values (list): List of fi values.

    Returns:
        list: List of piecewise linear polynomials.
    """
    n = len(xi_values)
    x = sym.Symbol('x')
    px_table = []

    tr = 1
    while not(tr >= n):
        numerator = fi_values[tr] - fi_values[tr - 1]
        denominator = xi_values[tr] - xi_values[tr - 1]
        m = numerator / denominator
        px_tr = fi_values[tr - 1] + m * (x - xi_values[tr - 1])
        px_table.append(px_tr)
        tr = tr + 1

    return px_table

def create_matrix(n):
    """
    Create an n x m matrix.

    Args:
        n (int): Number of rows.

    Returns:
        list: A list of user input data.
    """
    matrix = []
    n = int(n)
    matrix = [float(input("Input data: ")) for i in range(n)]
    return matrix

size = input("Input the size of the arrays: ")
print("Input your xi values: ")
xi_values = create_matrix(size)
print("Input your fi values: ")
fi_values = create_matrix(size)
samples = int(input("Input the number of samples: "))
n = len(xi_values)
px_table = lineal_interpolation(xi_values, fi_values)

print('Piecewise linear polynomials:')
for tr in range(1, n):
    print('  x = [' + str(xi_values[tr - 1]) + ',' + str(xi_values[tr]) + ']')
    print(str(px_table[tr - 1]))

x_trz = np.array([])
y_trz = np.array([])
tr = 1
while not(tr >= n):
    a = xi_values[tr - 1]
    b = xi_values[tr]
    x_tr = np.linspace(a, b, samples)
    px_tr = px_table[tr - 1]
    pxt = sym.lambdify('x', px_tr)
    y_tr = pxt(x_tr)
    x_trz = np.concatenate((x_trz, x_tr))
    y_trz = np.concatenate((y_trz, y_tr))
    tr = tr + 1

# Make the graph
plt.plot(xi_values, fi_values, 'o', label='Points')
plt.plot(x_trz, y_trz, label='Interpolated')
plt.title('Linear Interpolation')
plt.xlabel('xi')
plt.ylabel('px(xi)')
plt.legend()
plt.show()
