import math

def findRoot(f,a,b,epsilon):
    while math.fabs(a-b)>epsilon:
        m=(a+b)/2
        if f(m)==0:
            break
        elif f(a)*f(m)<0:
            b=m
        else:
            a=m
    return m
