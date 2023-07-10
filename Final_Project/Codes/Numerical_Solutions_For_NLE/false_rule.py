import sympy as sp
import numpy as np

x = sp.symbols('x')

def create_symbolic_function(expression):
    global x
    return sp.sympify(expression)

def false_rule(eq, a, b, tol):
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


function_expression = input("Enter the function expression: ")
a = float(input("Enter a: "))
b = float(input("Enter b: "))
tolerance = float(input("Enter the tolerance: "))

false_rule(function_expression, a, b, tolerance)


