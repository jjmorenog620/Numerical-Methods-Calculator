import sympy as sp
x=sp.symbols('x')

def function(eq):
    global x
    return sp.sympify(eq)

def PF(eq,x0,tol,maxite):
    global x
    eq=function(eq)+x 
    e=0
    i=0 
    while maxite>i:
        xi=eq.evalf(subs={x:x0}) 
        e=abs(xi-x0)
        if e<tol:
            print('The solution is in '+ str(x0)+', with an eror of '+str(e))
            break
        i=i+1
        x0=xi
   
    
    
fun = input("Put the Function: ")
x0 = float(input("Put X0: "))
e = float(input("Put tolerancie: "))
it=float(input("Put max ite: "))
PF(fun,x0,e,it)


