from matplotlib import pyplot as plt
import numpy as np
import sys


def center_heightmap(factor):
    side = 2**int(factor) + 1
    size = (side, side)
    img = np.zeros(size)

    img[int(side/2)][int(side/2)] = 5

    plt.imsave(f"{'1'}.png", img, cmap="gray")


if __name__ == '__main__':
    center_heightmap(sys.argv[1])
