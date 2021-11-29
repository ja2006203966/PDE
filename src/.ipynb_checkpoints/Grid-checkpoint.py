import numpy as np
import copy
from src.Space import Space

def _quick(shape, a, func, n, diff):
    a = copy.copy(a)
    func = copy.copy(func)
    b = a.take(np.arange(shape[n]-1, shape[n]), axis=n) + diff
    b = np.append( a.take(np.arange(1, shape[n]), axis=n), b , axis=n)
    b = b-a
    b = b.take(np.arange(n, n+1), axis=-1)
    
    delta_f0 = func.take(np.arange(n, n+1), axis=-1) # change for (binx, biny, binz, 3) => (binx, biny, binz, 1) 
    delta_f = delta_f0.take(np.arange(shape[n]-1, shape[n]), axis=n)
    delta_f = np.append(delta_f0.take(np.arange(1,shape[n]), axis=n), delta_f, axis=n)
    delta_f = delta_f -func.take(np.arange(n, n+1), axis=-1)
    delta_f = delta_f/diff
    
#     delta_f = func.take(np.arange(shape[n]-1, shape[n]), axis=n)
#     delta_f = np.append(func.take(np.arange(1,shape[n]), axis=n), delta_f, axis=n)
# #     delta_f = delta_f.take(np.arange(n, n+1), axis=-1)
#     delta_f = delta_f -func
#     delta_f = delta_f/diff
#     delta_f = delta_f.take(np.arange(n, n+1), axis=-1)
    

    return b, copy.copy(delta_f)

    
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
        grid = []
        if self.dimension >=1:
            self.delta_b1, self.u =_quick(shape, a, func, 0, self.space.b1_diff)
            grid.append(self.u)
        if self.dimension >=2:
            self.delta_b2, self.v =_quick(shape, a, func, 1, self.space.b2_diff)
            grid.append(self.v)
        if self.dimension >=3:
            self.delta_b3, self.w =_quick(shape, a, func, 2, self.space.b3_diff)
            grid.append(self.w)
#         self.grid = self.u + self.v + self.w
        grid = tuple(grid)
        self.grid = np.concatenate(grid, axis = -1)
        return self.grid
