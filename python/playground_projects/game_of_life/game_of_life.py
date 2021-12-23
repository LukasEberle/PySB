import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

x = np.random.choice([0, 255], 16*16, p=[0.1, 0.9]).reshape(16, 16)
plt.imshow(x, interpolation='nearest')


def addGlider(i, j, grid):
    """adds a glider with its top left cell at (i, j)"""
    glider = np.array([[0, 0, 255],
                       [255, 0, 255],
                       [0, 255, 255]])
    grid[i:i+3, j:j+3] = glider


if __name__ == "__main__":
    plt.show()
