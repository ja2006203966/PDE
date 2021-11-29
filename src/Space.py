import numpy as np
import copy
class Space:
    def __init__(self, basis: list, bins = (32, 32, 32)):
        self.bins = bins
        self.intervals = basis
        self.coordination = 'Catesian'
        self.dimension = len(basis)
        self.basis = []
        if self.dimension >=1:
            self.b1 = np.linspace(*basis[0], num = bins[0])
            self.b1_diff = (basis[0][1] - basis[0][0])/bins[0]
            self.basis.append(self.b1)
        if self.dimension >=2:
            self.b2 = np.linspace(*basis[1], num = bins[1])
            self.b2_diff = (basis[1][1] - basis[1][0])/bins[1]
            self.basis.append(self.b2)
        if self.dimension >=3:
            self.b3 = np.linspace(*basis[2], num = bins[2])
            self.b3_diff = (basis[2][1] - basis[2][0])/bins[2]
            self.basis.append(self.b3)
        basis_expand  = [[j for j in range(self.dimension) if j!=i] for i in range(self.dimension)]
        for i in range(self.dimension):
            for j in basis_expand[i]:
                self.basis[i] = np.expand_dims(self.basis[i], axis = j)
    def to_numpy(self,):
        basis_expand  = [[self.bins[j] if j!=i else 1 for j in range(self.dimension) ] for i in range(self.dimension)]
        basis  = copy.copy(self.basis)
        for i in range(self.dimension):
            basis[i] = np.tile(basis[i], tuple(basis_expand[i]) )
            basis[i] = np.expand_dims(basis[i], axis=-1)
        basis = tuple(basis)
        return np.concatenate(basis, axis=-1)
    
    
        