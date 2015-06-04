import numpy
from scipy.integrate import odeint

class Lorenz(object):
    def __init__(self, vector, sigma=10, rho=28, beta=8/3):
        self.vector = vector
        self.sigma = sigma
        self.rho = rho
        self.beta = beta
    
    def lor(self, x, t):
        x_dot = self.sigma*(x[1] - x[0])
        y_dot = x[0]*(self.rho - x[2]) - x[1]
        z_dot = x[0]*x[1] - self.beta*x[2]
        return [x_dot, y_dot, z_dot]
    
    def solve(self,T,dt):
        tijden = numpy.arange(0,T+dt,dt)
        return odeint(self.lor, self.vector, tijden)