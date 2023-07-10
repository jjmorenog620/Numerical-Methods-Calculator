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

def incremental_search(eq, a, b, delta_x):
    """
    Performs an incremental search to find an interval containing a root of the function.

    Args:
        eq (str): The mathematical equation representing the function.
        a (float): The lower bound of the search interval.
        b (float): The upper bound of the search interval.
        delta_x (float): The increment size for searching.

    Returns:
        tuple: The lower bound, upper bound, and the number of iterations.
    """
    global x
    eq = create_symbolic_function(eq)
    it = 0

    while a < b:
        xi = a + delta_x
        fun_a = eq.evalf(subs={x: a})    
        fun_xi = eq.evalf(subs={x: xi})
        if (fun_a * fun_xi) < 0:    
            it = it + 1         
            break
        else:
            it = it + 1
            a = xi
    print('The solution is in the interval [' + str(a) + ', ' + str(xi) + ']')
    
    return a, xi, it
          
# Prompt the user for function expression, lower bound, upper bound, and delta x
function_expression = input("Enter the function expression: ")
lower_bound = float(input("Enter the lower bound: "))
upper_bound = float(input("Enter the upper bound: "))
delta_x = float(input("Enter delta x: "))

# Perform incremental search
incremental_search(function_expression, lower_bound, upper_bound, delta_x)
