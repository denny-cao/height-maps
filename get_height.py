import numpy as np 
from PIL import Image


def height(file: str, x: float, y: float, max: float, scale=1.0) -> float:
    heightmap = np.asarray(Image.open(file).convert('L'))
    x, y = convert_to_array_index(x, y, scale)
    return scale_height(max, heightmap[y][x])
 

def convert_to_array_index(x, y, scale):
    '''
    Convert world coordinates to array indices
    '''

    # Shift indices to make top left point (0,0)
    x_index = x + scale
    y_index = abs(y - scale)
        
    # Ratio to get indice if top left point was (-x, y) -> Center is (0,0)
    x_index *= (64 / scale)
    y_index *= (64 / scale)

    return round(x_index), round(y_index)


def scale_height(max: float, current_height: int) -> float:
    '''
    Scale height from 0-255 to max height of world file
    '''
    
    return (current_height / 255) * max