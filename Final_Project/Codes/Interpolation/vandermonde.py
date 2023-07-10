import numpy as np
import sympy as sym
import matplotlib.pyplot as plt

def vandermonde_interpolation(xi_values, fi_values):
    """
    Perform Vandermonde interpolation using the given xi and fi values.

    Args:
        xi_values (list): List of xi values.
        fi_values (list): List of fi values.

    Returns:
        tuple: A tuple containing the Vandermonde matrix, coefficients, interpolated polynomial, x values, and y values.
    """
    samples = 101
    xi = np.array(xi_values)
    fi = np.array(fi_values)
    n = len(xi)

    # Create Vandermonde matrix
    A = np.zeros(shape=(n, n), dtype=float)
    for i in range(n):
        for j in range(n):
            power = (n - 1) - j
            A[i, j] = xi[i] ** power

    coefficients = np.linalg.solve(A, fi)  # Solve system
    x = sym.Symbol('x')
    polynomial = 0

    for i in range(n):
        power = (n - 1) - i
        term = coefficients[i] * (x ** power)
        polynomial += term

    px = sym.lambdify(x, polynomial)

    a = np.min(xi)
    b = np.max(xi)
    x_in = np.linspace(a, b, samples)
    y_in = px(x_in)
    return A, coefficients, polynomial, x_in, y_in

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

(A, coefficients, polynomial, x_in, y_in) = vandermonde_interpolation(xi_values, fi_values)

print('Vandermonde Matrix:')
print(A)
print('Polynomial Coefficients:')
print(coefficients)
print('Interpolated Polynomial:')
print(polynomial)

# Make the graph using plt
plt.plot(xi_values, fi_values, 'o', label='[xi, fi]')
plt.plot(x_in, y_in, label='p(x)')
plt.xlabel('xi')
plt.ylabel('fi')
plt.legend()
plt.title("Vandermonde Interpolation")
plt.show()
