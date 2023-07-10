import sympy as sp

x=sp.symbols('x')

def funtion(func):
    global x
    return sp.sympify(func)


def Bisec(func,a,b,tol):
    func=funtion(func)
    xr=0   
    ea=100     
    fa=func.evalf(subs={x: a}) 
    while ea>tol :
        xprev=xr
        xr=(a+b)/2
        fr=func.evalf(subs={x:xr})
        if xr != 0:
            ea=abs((xr-xprev)/xr)*100
        test=fa*fr                                   
        if test < 0 :
            b=xr
        elif test >0:
            a=xr
            fa=fr
        else:
            ea=0
    print('The solution is ' +str(xr), 'with an error of'+str(ea))
    
    
fun = input("Put the funtion:  ")
xl = float(input("Put a: "))
xu = float(input("Put b: "))
es = float(input("Put the tolerance: "))

Bisec(fun,xl,xu,es)
  
    
    


