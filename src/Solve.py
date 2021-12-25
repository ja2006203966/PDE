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
        w = self.condition -u -v
        return w
    def _quick(self, a, b, sp, diff, n):
        '''
        diff:
        a: dynamical ptential e.g. 3D shape = (binx, biny, dynamical binz)
        b: dynamical vector field = Gradient(a) e.g. 3D shape = (binx, biny,  dynamical binz, 3)
        c: Gradient(b) e.g. 3D shape = (binx, biny,  dynamical binz, 3)
        diff:difference of binn_(i) and binn_(i+1) n=x,y,z diff.shape = (dimension, )
        sp: coordinate e.g. 3D shape = (binx, biny, binz, 3)
        
        '''
#         shape = z.shape
        shape = a.shape
#         layer = z.take(np.arange(shape[n]-1, shape[n]), axis=n)
        un = n-1 if n-1 >=0 else self.space.dimension -1
        vn = un-1 if un-1 >=0 else self.space.dimension -2
#         u = self.gradient(shape, a, z, n, diff)
        u = self.gradient(shape, sp, a, un, diff[un])
        v = self.gradient(shape, sp, a, vn, diff[vn])
        du = self.gradient(shape, sp, b, un, diff[un])
        dv = self.gradient(shape, sp, b, vn, diff[vn])
#         w = self.start_from_z(u, v)
        dw = self.start_from_z(du, dv)
        b_last = b.take(np.arange(shape[n]-1, shape[n]), axis=n)
        b_add = b_last + dw*diff[n]
        a_last = a.take(np.arange(shape[n]-1, shape[n]), axis=n)
        a_add = a_last + w*diff[n]
        a = np.concatenate((a, a_add), axis = n)
        b = np.concatenate((b, w), axis = n)
        return a, b
    def DP(self, dL, layer, n, layer_stop, n_stop, diff):
        if n != n_stop:
            layer_next = layer + dL*diff
        else:
            return layer_stop
            
        
    def solve(self,):
        self.result = self.bc[-1][0] #start from lower bound of z axis (if dimension=3)
        self.vector = self.result*0 # (bins, bins, bins, 3)
        diff = self.space.diff
        N = self.bins[-1] - 1
        for i in range(N):
            self.result, self.vector = self._quick(self.result, self.vector)
        
        
