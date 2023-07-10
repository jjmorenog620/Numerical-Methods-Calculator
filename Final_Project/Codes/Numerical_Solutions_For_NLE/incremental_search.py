import sympy as sp

x = sp.symbols('x')

def create_symbolic_function(eq):
    global x
    return sp.sympify(eq)

def incremental_search(eq, a, b, delta_x):
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
          
function_expression = input("Enter the function expression: ")
a = float(input("Enter a: "))
b = float(input("Enter b: "))
delta_x = float(input("Enter delta x: "))

incremental_search(function_expression, a, b, delta_x)
