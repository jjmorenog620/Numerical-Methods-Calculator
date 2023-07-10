import sympy as sp
import numpy as np

x=sp.symbols('x')

def function(func):
    global x
    return sp.sympify(func)

def false_rule(eq,a,b,tol):
    global x
    eq=function(eq)
    e = abs(b-a)
    fa = eq.evalf(subs={x:a})
    fb = eq.evalf(subs={x:b})
    while not(e<=tol):
        c = b - fb*(a-b)/(fa-fb)
        fc = eq.evalf(subs={x:c})
        r = np.sign(fa)*np.sign(fc)
        
        if r>0:
            e = abs(c-a)
            a = c
            fa = fc
        else:
            e = abs(b-c)
            b = c
            fb = fc
    print('the solution is '+str(c)+ ', with an error of '+str(e))
    print(c)
    print(e)


fun = input("Put the function:  ")
a = float(input("Put a: "))
b = float(input("Put b: "))
tol = float(input("Put tolerance: "))

false_rule(fun,a,b,tol)

