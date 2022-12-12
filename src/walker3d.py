import random as rnd

class Lattice:
    def __init__(self, xl, yl, zl: int) -> None:
        self.xl = xl
        self.yl = yl
        self.zl = zl

class Walker3D:
    def __init__(self, nbr: int, xs: int, ys: int, zs: int) -> None:
        self.nbr = nbr
        self.xpos = xs
        self.ypos = ys
        self.zpos = zs
        self.alive = True

    def step(self, lattice: 'Lattice') -> None:
        dx, dy, dz = rnd.choices([0, 1, -1], k = 3)  #pick 3 updates
                
        if self.xpos == lattice.xl: #make sure walker doesn't escape
            self.xpos -= 1
        elif self.xpos == 0:
            self.xpos += 1
        elif self.ypos == lattice.yl:
            self.ypos -= 1
        elif self.ypos == 0:
            self.ypos += 1    
        elif self.zpos == lattice.zl:
            self.zpos -= 1
        elif self.zpos == 0:
            self.zpos += 1 
        else: 
            self.xpos += dx
            self.ypos += dy
            self.zpos += dz

    def collide(self, walkers: list) -> None:
        for walker in walkers:
            if walker.nbr != self.nbr:
                if walker.xpos == self.xpos and walker.ypos == self.ypos and walker.zpos == self.zpos:                    
                    self.alive = False
                    walker.alive = False
                else:
                    continue
            else:
                continue

