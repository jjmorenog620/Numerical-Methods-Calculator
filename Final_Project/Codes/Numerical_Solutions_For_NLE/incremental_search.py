import sympy as sp

x=sp.symbols('x')

def funcion(ecua):
    global x
    return sp.sympify(ecua)

def Incremental_Search(eq, a, b, deltaX):
    global x
    eq=funcion(eq)
    it=0

    while(a<b):
        xi = a + deltaX
        fun_a = eq.evalf(subs={x:a})    
        fun_xi = eq.evalf(subs={x:xi})
        if (fun_a *fun_xi )<0:    
          it=it+1         
          break
        else:
            it=it+1
            a=xi
    print('The solution is in the interval ['+str(a)+', '+ str(xi)+']')
    
    return a,xi,it
          
func = input("Put the function: ")
a = float(input("put a: "))
b = float(input("Put b: "))
dx = float(input("pt dx: "))

Incremental_Search(func,a,b,dx)




