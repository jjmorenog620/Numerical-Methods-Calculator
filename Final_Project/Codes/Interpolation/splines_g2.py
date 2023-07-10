import numpy as np
import sympy as sym
import matplotlib.pyplot as plt

def spline_natural(xi_values, yi_values):
    """
    Perform natural cubic spline interpolation using the given xi and yi values.

    Args:
        xi_values (list): List of xi values.
        yi_values (list): List of yi values.

    Returns:
        list: List of piecewise polynomial equations.
    """
    n = len(xi_values)
    h = np.zeros(n - 1, dtype=float)

    for j in range(0, n - 1):
        h[j] = xi_values[j + 1] - xi_values[j]

    A = np.zeros(shape=(n - 2, n - 2), dtype=float)
    B = np.zeros(n - 2, dtype=float)
    S = np.zeros(n, dtype=float)

    A[0, 0] = 2 * (h[0] + h[1])
    A[0, 1] = h[1]
    B[0] = 6 * ((yi_values[2] - yi_values[1]) / h[1] - (yi_values[1] - yi_values[0]) / h[0])

    for i in range(1, n - 3):
        A[i, i - 1] = h[i]
        A[i, i] = 2 * (h[i] + h[i + 1])
        A[i, i + 1] = h[i + 1]
        fac21 = (yi_values[i + 2] - yi_values[i + 1]) / h[i + 1]
        fac10 = (yi_values[i + 1] - yi_values[i]) / h[i]
        B[i] = 6 * (fac21 - fac10)

    A[n - 3, n - 4] = h[n - 3]
    A[n - 3, n - 3] = 2 * (h[n - 3] + h[n - 2])
    fac12 = (yi_values[n - 1] - yi_values[n - 2]) / h[n - 2]
    fac23 = (yi_values[n - 2] - yi_values[n - 3]) / h[n - 3]
    B[n - 3] = 6 * (fac12 - fac23)

    r = np.linalg.solve(A, B)

    for j in range(1, n - 1):
        S[j] = r[j - 1]
    S[0] = 0
    S[n - 1] = 0

    a = np.zeros(n - 1, dtype=float)
    b = np.zeros(n - 1, dtype=float)
    c = np.zeros(n - 1, dtype=float)
    d = np.zeros(n - 1, dtype=float)

    for j in range(0, n - 1):
        a[j] = (S[j + 1] - S[j]) / (6 * h[j])
        b[j] = S[j] / 2
        fac10 = (yi_values[j + 1] - yi_values[j]) / h[j]
        c[j] = fac10 - (2 * h[j] * S[j] + h[j] * S[j + 1]) / 6
        d[j] = yi_values[j]

    x = sym.Symbol('x')
    px_table = []

    for j in range(0, n - 1):
        pxtr = a[j] * (x - xi_values[j]) ** 3 + b[j] * (x - xi_values[j]) ** 2
        pxtr += c[j] * (x - xi_values[j]) + d[j]
        pxtr = pxtr.expand()
        px_table.append(pxtr)

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
print("Input your yi values: ")
yi_values = create_matrix(size)
samples = int(input("Input the number of samples: "))
n = len(xi_values)
px_table = spline_natural(xi_values, yi_values)

print('Piecewise polynomial:')
for tr in range(1, n):
    print(' x = [' + str(xi_values[tr - 1]) + ',' + str(xi_values[tr]) + ']')
    print(str(px_table[tr - 1]))

x_trz = np.array([])
y_trz = np.array([])
tr = 1
while not(tr >= n):
    a = xi_values[tr - 1]
    b = xi_values[tr]
    x_tr = np.linspace(a, b, samples)

    # Evaluate polynomial
    px_tr = px_table[tr - 1]
    pxt = sym.lambdify('x', px_tr)
    y_tr = pxt(x_tr)

    # Vectors for x and y
    x_trz = np.concatenate((x_trz, x_tr))
    y_trz = np.concatenate((y_trz, y_tr))
    tr = tr + 1

# Make the graph
plt.plot(xi_values, yi_values, 'ro', label='Points')
plt.plot(x_trz, y_trz, label='Interpolated', color='green')
plt.title('Natural Cubic Spline')
plt.xlabel('xi')
plt.ylabel('px(xi)')
plt.legend()
plt.show()
