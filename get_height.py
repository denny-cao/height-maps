import numpy as np 
from pillow import Image


def height(file: str, x: float, y: float, max: float) -> float:
    heightmap = np.asarray(Image.open(file).convert('L'))
    x, y = convert_to_array_index(x, y)
    return scale_height(max, heightmap[y][x])
 

def convert_to_array_index(x, y):
    '''
    Convert world coordinates to array indices
    '''
    # Ratio to get indice if top left point was (-65, 65) -> Center is (0,0)
    x_index = x * 64
    y_index = y * 64

    # Shift indices to make top left point (0,0) instead of (-65, 65)
    x_index += 64
    y_index -= 64

    return round(x_index), round(y_index)


def scale_height(max: float, current_height: int) -> float:
    '''
    Scale height from 0-255 to max height of world file
    '''
    return (current_height / 255) * max







    

