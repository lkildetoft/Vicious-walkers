import src.walkersim as ws

def main() -> None:
    print("Please input lattice dimensions (x, y, z):")
    l_dim = str(input()).split(",")
    print("Please input the number of iterations (integer):")
    n_iter = int(input())
    print("Please input the number of walkers (integer):")
    n_walkers = int(input())
    print("Please input the desired fps (decimal)")
    fps = float(input())
    sim = ws.WalkerSimulator(xl = int(l_dim[0]), yl = int(l_dim[1]), zl = int(l_dim[2]), n_walkers = n_walkers, n_iterations = n_iter, fps = fps)
    print("Running simulation...please wait")
    sim.run()

if __name__ == "__main__":
    main()