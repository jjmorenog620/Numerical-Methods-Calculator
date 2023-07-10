import numpy as np
import sympy as sym
import matplotlib.pyplot as plt

def calculate_divided_differences(x_values, f_values):
    """
    Calculates the divided differences and returns the polynomial, x points, and y points.

    Args:
        x_values (list): List of x values.
        f_values (list): List of f values (y values).

    Returns:
        tuple: A tuple containing the polynomial, x points, and y points.
    """
    x = sym.Symbol('x')  # Symbolic variable for polynomial expression
    x_i = np.array(x_values, dtype=float)  # Convert x values to a NumPy array
    f_i = np.array(f_values, dtype=float)  # Convert f values to a NumPy array
    n = len(x_i)  # Number of data points

    board = np.zeros(shape=(n, n), dtype=float)  # Create a square matrix to store divided differences
    board[:, 0] = x_i  # Set the first column of the matrix as x_i values
    board[:, 1] = f_i  # Set the second column of the matrix as f_i values

    # Calculate divided differences recursively
    for j in range(2, n + 1):
        for i in range(n - j + 1):
            denominator = (board[i + j - 1, 0] - board[i, 0])  # Calculate denominator for the divided difference
            numerator = board[i + 1, j - 1] - board[i, j - 1]  # Calculate numerator for the divided difference
            board[i, j] = numerator / denominator  # Store the divided difference in the matrix

    p_xi = np.linspace(np.min(x_i), np.max(x_i), num=101)  # Generate x points for plotting
    p_fi = np.zeros_like(p_xi)  # Initialize an array to store the evaluated polynomial at x points

    # Evaluate the polynomial using Horner's method
    for i in range(n):
        term = board[0, i + 1]  # Get the coefficient of the current term
        for j in range(i):
            term *= (x - board[j, 0])  # Multiply the term by (x - x_i)
        p_fi += term  # Add the current term to the polynomial

    p_x = sym.lambdify(x, p_fi)  # Convert the polynomial expression to a callable function
    p_fi = p_x(p_xi)  # Evaluate the polynomial at the x points

    return p_fi, p_xi, p_fi  # Return the polynomial, x points, and y points


def define_matrix(size):
    """
    Prompts the user to input data and returns a list.

    Args:
        size (int): Size of the data list.

    Returns:
        list: A list of user input data.
    """
    matrix = []
    size = int(size)
    matrix = [float(input("Input data: ")) for _ in range(size)]
    return matrix

array_size = input("Input the size of the arrays: ")
print("Input x values: ")
x_i_values = define_matrix(array_size)  # List of x values
print("Input f values: ")
f_i_values = define_matrix(array_size)  # List of f values (y values)

poly, p_xi, p_fi = calculate_divided_differences(x_i_values, f_i_values)
print("Polynomial: ", poly)

# Graph
plt.plot(x_i_values, f_i_values, 'o', label='Points')  # Plotting the input points
plt.plot(p_xi, p_fi, label='Polynomial')  # Plotting the polynomial curve
plt.legend()
plt.xlabel('x_i')
plt.ylabel('f_i')
plt.title(poly)
plt.show()
