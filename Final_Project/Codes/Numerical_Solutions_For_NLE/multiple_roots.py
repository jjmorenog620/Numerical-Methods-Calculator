import sympy as sp

x = sp.symbols('x')

def create_symbolic_function(eq):
    global x
    return sp.sympify(eq)

def multiple_roots(eq, x0, tol, max_iterations):
    global x
    eq = create_symbolic_function(eq)
    d1 = sp.diff(eq, x)
    d2 = sp.diff(d1, x)

    c = 0
    e = tol + 1

    while c < max_iterations and e > tol and ((pow(d1.evalf(subs={x: x0}), 2) - (eq.evalf(subs={x: x0}) * d2.evalf(subs={x: x0}))) != 0):
        c = c + 1
        t = x0 - ((eq.evalf(subs={x: x0}) * d1.evalf(subs={x: x0})) / (pow(d1.evalf(subs={x: x0}), 2) - (eq.evalf(subs={x: x0}) * d2.evalf(subs={x: x0}))))
        e = abs(x0 - t)
        x0 = t
    print('The solution is ' + str(x0) + ', with an error of ' + str(e))
    
function_expression = input("Enter the function expression: ")
x0 = float(input("Enter x0: "))
tolerance = float(input("Enter the tolerance: "))
max_iterations = int(input("Enter maximum iterations: "))

multiple_roots(function_expression, x0, tolerance, max_iterations)
