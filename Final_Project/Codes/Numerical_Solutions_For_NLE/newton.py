import sympy as sp

x=sp.symbols('x')

def function(eq):
    global x
    return sp.sympify(eq)

def Newton(eq,x_0,es,maxIte):
    global x
    eq=function(eq)
    d=sp.diff(eq)
    f_NR=x-(eq/d)
    ea=100 
    x_r=x_0
    inter=0
    while ea>es:
        x_prev=x_r
        x_r=f_NR.evalf(subs={x:x_prev})
        if x_r !=0:
            ea=abs((x_r-x_prev)/x_r)*100
        inter+=1
        
        if inter>=maxIte:
            break
        
    print('The solution is '+str(x_r)+', with an eror of '+str(ea)+', in '+ str(inter)+ ' iterations')
    
fun=input("Put the function: ")
x_0=float(input("Put X0: "))
tol=float(input("Put tolerance: "))
maxIte=int(input("Put max iterations: "))
Newton(fun,x_0,tol,maxIte)
    
