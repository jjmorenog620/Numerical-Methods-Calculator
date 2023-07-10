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

def newton(eq, x_0, es, max_iterations):
    """
    Performs the Newton's method to find a root of a function.

    Args:
        eq (str): The mathematical equation representing the function.
        x_0 (float): The initial guess for the root.
        es (float): The desired tolerance for the root.
        max_iterations (int): The maximum number of iterations to perform.

    Returns:
        None
    """
    global x
    eq = create_symbolic_function(eq)
    d = sp.diff(eq)
    f_NR = x - (eq / d)
    ea = 100
    x_r = x_0
    iterations = 0

    while ea > es:
        x_prev = x_r
        x_r = f_NR.evalf(subs={x: x_prev})
        if x_r != 0:
            ea = abs((x_r - x_prev) / x_r) * 100
        iterations += 1

        if iterations >= max_iterations:
            break

    print('The solution is ' + str(x_r) + ', with an error of ' + str(ea) + ', in ' + str(iterations) + ' iterations')
    
# Prompt the user for function expression, initial guess, tolerance, and maximum iterations
function_expression = input("Enter the function expression: ")
x_0 = float(input("Enter X0: "))
tolerance = float(input("Enter tolerance: "))
max_iterations = int(input("Enter max iterations: "))

# Perform Newton's method
newton(function_expression, x_0, tolerance, max_iterations)
