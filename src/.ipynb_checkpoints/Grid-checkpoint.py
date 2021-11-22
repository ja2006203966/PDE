import numpy as np
import copy
from src.Space import Space

def _quick(shape, a, func, n):
    b = a.take(np.arange(shape[n]-1, shape[n]), axis=n)
    b = np.append(a.take(np.arange(1, shape[n]), axis=n), b, axis=n)
    delta_f = func.take(np.arange(shape[n]-1, shape[n]), axis=n)
    delta_f = np.append(func.take(np.arange(1,shape[n]), axis=n), delta_f, axis=n)
    return b.take(np.arange(n,n+1), axis = -1), copy.copy(delta_f)
    
class Gradient:
    def __init__(self, f, space:Space, coordination = 'Catesian'):
        self.f = f
        self.space = space
        self.coordination = coordination
        self.u, self.v, self.w = 0,0,0
        self.dimension = space.dimension
        
    def Catesian(self,):
        a = self.space.to_numpy()
        func = self.f(a)
        shape = a.shape
        if self.dimension >=1:
            self.delta_b1, self.u =_quick(shape, a, func, 0)
        if self.dimension >=2:
            self.delta_b2, self.v =_quick(shape, a, func, 1)
        if self.dimension >=3:
            self.delta_b3, self.w =_quick(shape, a, func, 2)
        self.grid = self.u + self.v + self.w
        return self.grid
        