import numpy as np
import matplotlib.pyplot as plt

def interpolation(x_values, y_values):
    '''
    Perform interpolation using the given x and y values.

    Args:
        x_values (list): List of x values.
        y_values (list): List of y values.

    Returns:
        list: A list containing x and y values of the interpolated curve.
    '''
    x_values = np.array(x_values)  # Convert x values to NumPy array
    y_values = np.array(y_values)  # Convert y values to NumPy array
    length_of_x = len(x_values)

    A = np.zeros((length_of_x, length_of_x))  # Create a square matrix of zeros
    for i in range(length_of_x):
        A.T[i] = x_values ** i  # Assign powers of x to each column of the matrix
    coefficients = np.linalg.solve(A, y_values)  # Solve the linear system of equations

    x_theoretical = np.linspace(min(x_values), max(x_values), 100)  # Generate x values for the interpolated curve
    y_theoretical = np.zeros_like(x_theoretical)  # Initialize an array to store the interpolated y values

    for i in range(length_of_x):
        y_theoretical += coefficients[i] * x_theoretical ** i  # Compute the interpolated y values

    interpolated_values = [[], []]  # List to store interpolated x and y values
    for i in range(len(x_theoretical)):
        interpolated_values[0].append(x_theoretical[i])
        interpolated_values[1].append(y_theoretical[i])

    return interpolated_values

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
    matrix = [float(input('Input your data: ')) for _ in range(n)]
    return matrix

size = input("Input the size of the arrays: ")

print("Input your x values: ")
x_values = create_matrix(size)
print("Input your y values: ")
y_values = create_matrix(size)

interpolated_points = interpolation(x_values, y_values)

print("x\t\t\ty")
for i in range(len(interpolated_points[0])):
    print(interpolated_points[0][i], "\t", interpolated_points[1][i])

# Plot the interpolated curve

plt.plot(x_values, y_values, 'ro', label='Original Data')
plt.plot(interpolated_points[0], interpolated_points[1], 'b-', label='Interpolated Curve')
plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.title("Interpolation")
plt.show()
