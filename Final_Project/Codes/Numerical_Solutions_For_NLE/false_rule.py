import sympy as sp
import numpy as np

x = sp.symbols('x')

def create_symbolic_function(expression):
    """
    Creates a symbolic function from the given expression.

    Args:
        expression (str): The mathematical expression representing the function.

    Returns:
        sympy.Expr: The symbolic representation of the function.
    """
    global x
    return sp.sympify(expression)

def false_rule(eq, a, b, tol):
    """
    Performs the false position method to find the root of a function within a given interval.

    Args:
        eq (str): The mathematical expression representing the function.
        a (float): The lower bound of the interval.
        b (float): The upper bound of the interval.
        tol (float): The desired tolerance for the root.

    Returns:
        None
    """
    global x
    eq = create_symbolic_function(eq)
    e = abs(b - a)
    fa = eq.evalf(subs={x: a})
    fb = eq.evalf(subs={x: b})
    
    while not (e <= tol):
        c = b - fb * (a - b) / (fa - fb)
        fc = eq.evalf(subs={x: c})
        r = np.sign(fa) * np.sign(fc)
        
        if r > 0:
            e = abs(c - a)
            a = c
            fa = fc
        else:
            e = abs(b - c)
            b = c
            fb = fc
    
    print('The solution is ' + str(c) + ', with an error of ' + str(e))
    print(c)
    print(e)


# Prompt the user for function expression, lower bound, upper bound, and tolerance
function_expression = input("Enter the function expression: ")
a = float(input("Enter a: "))
b = float(input("Enter b: "))
tolerance = float(input("Enter the tolerance: "))

# Perform false position method
false_rule(function_expression, a, b, tolerance)
