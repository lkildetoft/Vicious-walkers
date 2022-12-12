import src.walker3d as w3d
import random as rnd
import matplotlib.pyplot as plt

class WalkerSimulator:
    def __init__(self, xl: int, yl: int, zl: int, n_walkers: int, n_iterations: int, fps: float) -> None:
        self.lattice = w3d.Lattice(xl, yl, zl)
        self.n_walkers = n_walkers
        self.n_iterations = n_iterations
        self.walkers = []
        self.walkerDecay = []
        self.fps = fps
        
    def __generateWalkers(self) -> None:
        for i in range(self.n_walkers):
            xs = rnd.randint(0, self.lattice.xl)
            ys = rnd.randint(0, self.lattice.yl)
            zs = rnd.randint(0, self.lattice.zl)
            self.walkers.append(w3d.Walker3D(i, xs, ys, zs))

    def __simulate(self) -> None:
        self.__generateWalkers()
        fig = plt.figure(figsize=plt.figaspect(2.))
        ax1 = fig.add_subplot(2, 1, 1, projection="3d")
        ax2 = fig.add_subplot(2, 1, 2)

        for n in range(self.n_iterations):
            ax1.clear()
            ax2.clear()

            xpos = []
            ypos = []
            zpos = []

            for walker in self.walkers:
                if walker.alive == False:
                    self.walkers.remove(walker)
                else:
                    walker.step(self.lattice)
                    walker.collide(self.walkers)

                xpos.append(walker.xpos)
                ypos.append(walker.ypos)
                zpos.append(walker.zpos)

            self.walkerDecay.append(len(self.walkers))

            ax1.set_xlim(0, self.lattice.xl)
            ax1.set_ylim(0, self.lattice.yl)
            ax1.set_zlim(0, self.lattice.zl)
            ax1.scatter(xpos, ypos, zpos, c = "b", marker = "o")
            ax2.plot(range(0, len(self.walkerDecay)), self.walkerDecay)

            plt.pause(1/self.fps)
      
    def run(self) -> None:
        self.__simulate()
        plt.show()
        plt.close()

