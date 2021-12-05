import numpy as np
import copy
from src.Space import Space
from src.Grid import Gradient
from src.Boundary import Boundary


class Solve_Laplace_Equation:
    def __init__(self, space:Space, boundary:Boundary, coordination = 'Catesian'):
        self.space = space
        self.bins = space.bins
        self.bc = boundary
        self.condition = 0
        self.gradient = Grid.gradient
    def start_from_z(self, b):
        # (w_i+1 - w_i)/diff_vector =  condition - (u_i+1 - u_i)/diff_vector - (v_i+1 - v_i)/diff_vector
#         w = self.condition -u -v
        return w
    def _quick(a, b, diff, n):
        shape = z.shape
        layer = z.take(np.arange(shape[n]-1, shape[n]), axis=n)
        un = n-1 if n-1 >=0 else self.space.dimension -1
        vn = un-1 if un-1 >=0 else self.space.dimension -2
        u = self.gradient(shape, a, z, n, diff)
        w = self.start_from_z(u, v)
        b = np.concatenate((b, w), axis = n)
        
        return a, b
    def solve(self,):
        self.result = self.bc[-1][0] #start from lower bound of z axis (if dimension=3)
        self.vector = self.result*0 # (bins, bins, bins, 3)
        diff = self.space.diff
        N = self.bins[-1] - 1
        for i in range(N):
            self.result, self.vector = self._quick(self.result, self.vector)
        
        
