import numpy as np
import sympy as sym
import matplotlib.pyplot as plt

def lagrange_interpolation(x_values, y_values):
    '''
    Perform Lagrange interpolation using the given x and y values.

    Args:
        x_values (list): List of x values.
        y_values (list): List of y values.

    Returns:
        tuple: A tuple containing the polynomial, x points, and y points.
    '''
    x_values = np.array(x_values)
    y_values = np.array(y_values)
    n = len(x_values)
    x = sym.Symbol('x')
    polynomial = 0
    div = np.zeros(n, dtype=float)

    for i in range(0, n):
        numerator = 1
        denominator = 1
        for j in range(0, n):
            if j != i:
                numerator *= (x - x_values[j])
                denominator *= (x_values[i] - x_values[j])
        Li = numerator / denominator

        polynomial += Li * y_values[i]
        div[i] = denominator

    simplified_polynomial = polynomial.expand()
    px = sym.lambdify(x, simplified_polynomial)

    num_samples = 101
    a = np.min(x_values)
    b = np.max(x_values)
    x_samples = np.linspace(a, b, num_samples)
    y_samples = px(x_samples)

    return simplified_polynomial, x_samples, y_samples

def create_matrix(n):
    '''
    Create an n x m matrix.

    Args:
        n (int): Number of rows.

    Returns:
        list: A list of user input data.
    '''
    matrix = []
    n = int(n)
    matrix = [float(input("Input data: ")) for _ in range(n)] 
    return matrix

size = input("Input the size of the arrays: ")
print("Input your x values: (float)")
x_values = create_matrix(size)
print("Input your y values: (float)")
y_values = create_matrix(size)

polynomial, x_samples, y_samples = lagrange_interpolation(x_values, y_values)
print("Polynomial: ", polynomial)

# Make chart with plt
plt.plot(x_values, y_values, 'o', label='Points')
plt.plot(x_samples, y_samples, label='Polynomial')
plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.title(polynomial)
plt.show()
