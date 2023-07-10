import sympy as sp

x = sp.symbols('x')

def create_symbolic_function(eq):
    global x
    return sp.sympify(eq)

def fixed_point(eq, x0, tol, max_iterations):
    global x
    eq = create_symbolic_function(eq) + x
    e = 0
    i = 0 
    while max_iterations > i:
        xi = eq.evalf(subs={x: x0}) 
        e = abs(xi - x0)
        if e < tol:
            print('The solution is in ' + str(x0) + ', with an error of ' + str(e))
            break
        i = i + 1
        x0 = xi
   
    
function_expression = input("Enter the function expression: ")
initial_guess = float(input("Enter initial guess (x0): "))
tolerance = float(input("Enter tolerance: "))
max_iterations = int(input("Enter maximum iterations: "))

fixed_point(function_expression, initial_guess, tolerance, max_iterations)



