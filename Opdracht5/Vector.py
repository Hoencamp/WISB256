from array import array

class Vector(object):
    def __init__(self, n, m=0):
        if type(m)==float or type(m)==int:
            self.vector = array('d',[m]*n)
        else:
            self.vector = array('d',m)
        self.n = n

    def __str__(self):
        x = ""
        for i in range(self.n):
            x = x+str(self.vector[i])+"\n"
        return x
        
    def lincomb(self,other,alpha,beta):
        w = array('d',[])
        for i in range(self.n):
            u = alpha*self.vector[i]
            v = beta*other.vector[i]
            w.append(u+v)
        return Vector(self.n, w)
    
    def scalar(self,alpha):
        y = self.lincomb(self,alpha,0)
        return y
    
    def inner(self,other):
        x=0
        for i in range(self.n):
            u = self.vector[i]
            v = other.vector[i]
            x = x+u*v
        return x
    
    def norm(self):
        x = self.inner(self)
        return x**0.5
    
u = Vector(3,[1,2,3])
v = Vector(3,3.5)
w = u.lincomb(v,10,1)
print(w)
w = w.scalar(2)
print(w)
print(w.norm())
print(w.inner(u))