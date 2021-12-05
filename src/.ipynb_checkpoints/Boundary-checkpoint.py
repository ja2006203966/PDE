import numpy as np
from src.Space import Space
import copy

def _quick(shape, a, func, n):
    al, au = a.take(np.arange(0, 1), axis=n), a.take(np.arange(shape[n]-1, shape[n]), axis=n)
    al, au = func[n][0](al), func[n][1](al)
#     a = a.take(np.arange(1, shape[n]-1), axis=n)
#     a = np.concatenate((al, a, au), axis = n)
#     return  a
    return al, au

def _quick_num(shape, a, num, n):
#     a = a.take(np.arange(1, shape[n]-1), axis=n)
    zero = a
    a = np.concatenate((num[0], a, num[1]), axis= n)
    return a

class Boundary:
    def __init__(self, space:Space, numercial_bc = 0, func = None, coordination = 'Catesian', types = "Analytic"):
        self.space = space
        self.numercial_bc = numercial_bc # ((x_lb, x_ub), (y_lb, y_up), (z_lb, z_up)), x_lb.shape = (1, binsy, binsz, number of dimensions) ...
        self.f = func # functions in tuple ((fxl, fxu), (fyl, fyu), (fzl, fzu))
        self.coordination = coordination
        self.dimension = space.dimension
        self.space_value = space.to_numpy()
        self.bounded_space = space.to_numpy()
        self.shape = self.bounded_space.shape
        self.types = types
    def mapping_anlaytic(self,):
        if self.dimension >=1:
#             self.bounded_space = _quick(self.shape, self.bounded_space, self.f, 0)
            self.bounded_space = _quick(self.shape, self.space_value, self.f, 0)
        if self.dimension >=2:
#             self.bounded_space = _quick(self.shape, self.bounded_space, self.f, 1)
            self.bounded_space = self.bounded_space + ((_quick(self.shape, self.space_value, self.f, 1)),)
        if self.dimension >=3:
#             self.bounded_space = _quick(self.shape, self.bounded_space, self.f, 2)
            self.bounded_space = self.bounded_space + ((_quick(self.shape, self.space_value, self.f, 2)),)
    def mapping_numercial(self,):
        if self.dimension >=1:
            self.bounded_space = _quick_num(self.shape, self.bounded_space, self.numercial_bc, 0)
        if self.dimension >=2:
            self.bounded_space = _quick_num(self.shape, self.bounded_space, self.numercial_bc, 1)
        if self.dimension >=3:
            self.bounded_space = _quick_num(self.shape, self.bounded_space, self.numercial_bc, 2)
    def get_bc(self,):
        if self.types == "Numercial":
#             self.mapping_numercial()
#             return self.bounded_space
            self.bounded_space = self.numercial_bc
            return self.numercial_bc
        if self.types == "Analytic":
            self.mapping_anlaytic()
            return self.bounded_space
        