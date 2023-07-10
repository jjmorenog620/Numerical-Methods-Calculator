import sympy as sp

x = sp.symbols('x')

def create_symbolic_function(expression):
    global x
    return sp.sympify(expression)


def bisecton(function, lower_bound, upper_bound, tolerance):
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


function_expression = input("Enter the function expression: ")
lower_bound = float(input("Enter the lower bound: "))
upper_bound = float(input("Enter the upper bound: "))
tolerance = float(input("Enter the tolerance: "))

bisecton(function_expression, lower_bound, upper_bound, tolerance)

  
    
    


