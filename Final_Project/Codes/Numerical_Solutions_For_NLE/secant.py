import sympy as sp

x = sp.symbols('x')

def create_symbolic_function(eq):
    """
    Creates a symbolic function from the given equation.

    Args:
        eq (str): The mathematical equation representing the function.

    Returns:
        sympy.Expr: The symbolic representation of the function.
    """
    global x
    return sp.sympify(eq)

def secant(fx, a, b, tol, max_iterations):
    """
    Performs the secant method to find a root of a function.

    Args:
        fx (str): The mathematical equation representing the function.
        a (float): The first initial guess.
        b (float): The second initial guess.
        tol (float): The desired tolerance for the root.
        max_iterations (int): The maximum number of iterations to perform.

    Returns:
        None
    """
    global x
    fx = create_symbolic_function(fx)
    e = tol + 1
    xi = a
    x0 = b
    c = 0

    while e > tol and c < max_iterations and (fx.evalf(subs={x: x0}) - fx.evalf(subs={x: xi})) != 0:
        c = c + 1
        x2 = x0 - ((fx.evalf(subs={x: x0}) * (x0 - xi)) / (fx.evalf(subs={x: x0}) - fx.evalf(subs={x: xi})))
        e = abs(xi - x0)
        x0 = xi
        xi = x2
    print('The solution is ' + str(x0) + ', with an error of ' + str(e))
    print(e)
              
# Prompt the user for function expression, initial guesses, tolerance, and maximum iterations
function_expression = input("Enter the function expression: ")
a = float(input("Enter a: "))
b = float(input("Enter b: "))
tolerance = float(input("Enter the tolerance: "))
max_iterations = int(input("Enter maximum iterations: "))

# Perform secant method
secant(function_expression, a, b, tolerance, max_iterations)
