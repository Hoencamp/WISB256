import random
import math
import sys

def drop_needle(L):
    x1=random.random()
    phi=random.vonmisesvariate(0,0)
    x2=x1+L*math.cos(phi)
    if x1==1 or x1==0:
        return True
    elif x2<=0 or x2>=1:
        return True
    else:
        return False

def estimate(N,L):
    x=0
    for i in range(N):
        if drop_needle(L)==True:
            x=x+1
    print(x, 'hits in', N, 'tries\nPi =', 2*L*N/x)

if not (len(sys.argv)==3 or len(sys.argv)==4):
    print('Use: estimate_pi.py N L')
elif float(sys.argv[2])>1.0:
    print('AssertionError: L should be smaller than 1')
elif len(sys.argv)==3:
    estimate(int(sys.argv[1]),float(sys.argv[2]))
else:
    zaad=sys.argv[3]
    random.seed(zaad)
    estimate(int(sys.argv[1]),float(sys.argv[2]))