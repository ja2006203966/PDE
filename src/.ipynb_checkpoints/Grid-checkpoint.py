import numpy as np
import copy
from src.Space import Space

class Gradient:
    def __init__(self, f, space:Space, coordination = 'Catesian'):
        self.f = f
        self.space = space
        self.coordination = coordination
        self.u, self.v, self.w = 0,0,0
        
    def Catesian(self,):
        a = self.space.to_numpy()
        func = self.f(a)
        if self.dimension >=1:
            b = a[-1:, :, : ,:]
            b = np.append(a[1:, :, : ,:], b, axis=0)
            delta_f = func[-1:, :, :, :]
            delta_f = np.append(func[1:, :, : ,:], delta_f, axis=0)
            self.delta_b1 = b[:, :, :, 0:1]
            self.u = copy.copy(delta_f)
            del(delta_f)
            del(b)
        if self.dimension >=2:
            b = a[:, -1:, : ,:]
            b = np.append(a[:, 1:, : ,:], b, axis=1)
            delta_f = func[:, -1:, : ,:]
            delta_f = np.append(func[:, 1:, : ,:], delta_f, axis=1)
            self.delta_b1 = b[:, :, :, 1:2]
            self.u = copy.copy(delta_f)
            del(delta_f)
            del(b)
        if self.dimension >=3:
            b = a[:, :, -1:, :]
            b = np.append(a[:, :, 1:, :], b, axis=2)
            delta_f = func[:, :, -1:, :]
            delta_f = np.append(func[:, :, 1:, :], delta_f, axis=2)
            self.delta_b1 = b[:, :, :, 2:3]
            self.u = copy.copy(delta_f)
            del(delta_f)
            del(b)
        self.grid = self.u + self.v + self.w
        return self.gird
        