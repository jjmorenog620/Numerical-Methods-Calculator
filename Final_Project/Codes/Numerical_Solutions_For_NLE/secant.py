import sympy as sp
x=sp.symbols('x')

def function(eq):
    global x
    return sp.sympify(eq)

def secant(fx,a,b,tol,it):
    global x
    fx=function(fx)
    e=tol+1
    xi=a
    x0=b
    c=0
   
    while (e>tol and c<it and (fx.evalf(subs={x:x0})-fx.evalf(subs={x:xi}))!=0):
        c=c+1
        x2=x0-((fx.evalf(subs={x:x0})*(x0-xi))/(fx.evalf(subs={x:x0})-fx.evalf(subs={x:xi})))
        e=abs(xi-x0)
        x0=xi
        xi=x2
        print('The solution is '+ str(x0)+ ', with an eror of '+str(e))
        print(e)
              
fun = input("Put the function: ")
a = float(input("Put a: "))
b = float(input("Put b: "))
tol = float(input("Put the tolerance: "))
ite = float(input("Put max iterations: "))


secant(fun,a,b,tol,ite)


