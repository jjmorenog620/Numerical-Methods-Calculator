import sympy as sp

x = sp.symbols('x')

def create_symbolic_function(eq):
    global x
    return sp.sympify(eq)

def newton_method(eq, x_0, es, max_iterations):
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
    
function_expression = input("Enter the function expression: ")
x_0 = float(input("Enter X0: "))
tolerance = float(input("Enter tolerance: "))
max_iterations = int(input("Enter max iterations: "))

newton_method(function_expression, x_0, tolerance, max_iterations)
