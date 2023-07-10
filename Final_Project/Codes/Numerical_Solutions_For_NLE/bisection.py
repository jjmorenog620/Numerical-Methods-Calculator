import sympy as sp

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


def bisection(function, lower_bound, upper_bound, tolerance):
    """
    Performs the bisection method to find the root of a function within a given interval.

    Args:
        function (str): The mathematical expression representing the function.
        lower_bound (float): The lower bound of the interval.
        upper_bound (float): The upper bound of the interval.
        tolerance (float): The desired tolerance for the root.

    Returns:
        None
    """
    function = create_symbolic_function(function)
    xr = 0   
    ea = 100     
    fa = function.evalf(subs={x: lower_bound}) 
    while ea > tolerance:
        xprev = xr
        xr = (lower_bound + upper_bound) / 2
        fr = function.evalf(subs={x: xr})
        if xr != 0:
            ea = abs((xr - xprev) / xr) * 100
        test = fa * fr                                   
        if test < 0:
            upper_bound = xr
        elif test > 0:
            lower_bound = xr
            fa = fr
        else:
            ea = 0
    print('The solution is ' + str(xr), 'with an error of ' + str(ea))


# Prompt the user for function expression, lower bound, upper bound, and tolerance
function_expression = input("Enter the function expression: ")
lower_bound = float(input("Enter the lower bound: "))
upper_bound = float(input("Enter the upper bound: "))
tolerance = float(input("Enter the tolerance: "))

# Perform bisection method
bisection(function_expression, lower_bound, upper_bound, tolerance)
