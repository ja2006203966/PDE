class Plot_Vector:
    def __init__(self, sp:Space, gd:np.ndarray):
        self.space = sp
        self.sp_np = sp.to_numpy()
        self.gd = gd
    def plot_3D(self,figsize = (16,16)):
        space = self.sp_np
        cas = self.gd
        fig = plt.figure(figsize = figsize)
        ax = fig.gca(projection='3d')
        ax = fig.gca()
        x, y, z =  space[:,:,:,0], space[:,:,:,1], space[:,:,:,2]
        u, v, w = cas[:,:,:,0], cas[:,:,:,1], cas[:,:,:,2]
        ax.quiver(x, y, z, u, v, w, length=0.8, alpha=0.1)
        plt.show()
    def plot_2D(self, figsize = (16,16), axis=0, index = 10):
        space = self.sp_np
        cas = self.gd
        fig = plt.figure(figsize = figsize)
        ax = fig.gca()
        # x, y, z =  space[:,:,:,0], space[:,:,:,1], space[:,:,:,2]
        # u, v, w = cas[:,:,:,0], cas[:,:,:,1], cas[:,:,:,2]
        # ax.quiver(x, y, z, u, v, w, length=0.4, alpha=0.1)
        # x, y = x[:,:,10], y[:,:,10]
        # u, v = u[:,:,10], v[:,:,10]
        cors = [i for i in range(3) if i!=axis]
        x = space[:,:,:,cors[0]].take(index, axis=axis)
        y = space[:,:,:,cors[1]].take(index, axis=axis)
        u = cas[:,:,:,cors[0]].take(index, axis=axis)
        v = cas[:,:,:,cors[1]].take(index, axis=axis)
        ax.quiver(x, y, u, v)
        plt.show()



