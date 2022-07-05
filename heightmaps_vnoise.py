from vnoise import Noise
import numpy as np
from matplotlib import pyplot as plt
import argparse
from random import seed 

def height_map(amount: int, scale: np.float64, octaves: np.float64, persistence: np.float64, lacunarity: np.float64) -> None: 
    noise = Noise()

    shape = (129, 129)
    repeat = (129, 129)


    for number in range(amount):
        noise.seed(seed())
        heightmap = np.zeros(shape, dtype=np.float64)
        for i in range(shape[0]):
            for j in range(shape[1]):
                heightmap[j][i] = noise.noise2(x=j / scale, y=i / scale, octaves=octaves, persistence=persistence, lacunarity=lacunarity, repeat_x=repeat[0], repeat_y=repeat[1], base=0)
        
        # Normalize Heightmap
        max = np.amax(heightmap)
        min = np.amin(heightmap)
        max -= min

        for y in range(shape[1]):
            for x in range(shape[0]):
                heightmap[y][x] -= min
                heightmap[y][x] /= max
    
        plt.imsave(f"{'0' * (len(str(amount)) - len(str(number)))}{number}.png", heightmap, cmap="gray")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Create heightmaps')
    parser.add_argument('-a', dest='amount', type=int, help='amount of heightmaps to generate', default=1)
    parser.add_argument('-s', dest='scale', type=np.float64, help='distance to view noisemap', default=50.0)
    parser.add_argument('-o', dest='octaves', type=int, help='how many layers of noise to add (Adjusts LOD)', default=1)
    parser.add_argument('-p', dest='persistence', type=np.float64, help='how much each octave contributes to shape (Adjusts amplitude)', default=1)
    parser.add_argument('-l', dest='lacunarity', type=np.float64, help='how much detail added or removed at each later octave (Adjusts frequency)', default=1)

    args = parser.parse_args()

    height_map(args.amount, args.scale, args.octaves, args.persistence, args.lacunarity)