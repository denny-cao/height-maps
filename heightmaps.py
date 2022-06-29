from noise import pnoise2
import numpy as np
from matplotlib import pyplot as plt
from random import randint
import sys


def height_map(amount):
    shape = (33, 33)
    repeat = (2048, 2048)
    scale = 50.0
    for number in range(amount + 1):
        heightmap = np.zeros(shape)
        base = randint(0 ,1000)
        for i in range(shape[0]):
            for j in range(shape[1]):
                noise_val = pnoise2(i/scale, j/scale, octaves=3, base=base, repeatx=repeat[0], repeaty=repeat[1])
                noise_val += 0.5 * pnoise2(i/scale, j/scale, octaves=6, base=base, repeatx=repeat[0], repeaty=repeat[1])
                noise_val += 0.25 *  pnoise2(i/scale, j/scale, octaves=12, base=base, repeatx=repeat[0], repeaty=repeat[1])
                noise_val += 0.125 * pnoise2(i/scale, j/scale, octaves=24, base=base, repeatx=repeat[0], repeaty=repeat[1])
                
                heightmap[i][j] = noise_val
                '''
                heightmap[i][j] = pnoise2(i/scale, 
                                            j/scale, 
                                            octaves=octaves,
                                            repeatx=512, 
                                            repeaty=512, 
                                            base=base)
                ''' 
        plt.imsave(f"{'0' * (len(str(amount)) - len(str(number)))}{number}.png", heightmap, cmap="gray")
    '''
    source /opt/ros/melodic/setup.bash
source ~/franka_ros_ws/devel/setup.bash

# Current issues: Gazebo not running when CMD command "gazebo." When I run gazebo with ros it doesn't work; link0 isn't linked to world?
# Can't get heightmaps to work

    '''

if __name__ == "__main__":
    height_map(int(sys.argv[1]))