import matplotlib.pyplot as plt
import numpy as np
import time


def mandelbrot_rec(c, I, z0: int=0):
    '''
    Recursion to determine if point is in set or not.

    Params:
    c  -> complex number
    I  -> max iteration count
    z0 -> initial state (default:0)
    '''
    z0 = z0**2 + c
    if I <= 0:
        return 0
    elif abs(z0) > 2:
        return I
    
    return mandelbrot_rec(c, I - 1, z0)


def draw_mandelbrot(x, y):
    grid = np.zeros((len(x),len(y)))
    for i, row in enumerate(x):
        for j, col in enumerate(y):
            grid[i, j] = mandelbrot_rec(complex(row,col), 100)
    plt.gcf().set_facecolor("black")
    plt.imshow(grid.T, extent=(x.min(), x.max(), y.min(), y.max()), cmap='hot', origin='lower')


def myb_optimized_draw_mandelbrot(x, y):
    grid = np.zeros((len(x), len(y)))
    vfunc = np.vectorize(mandelbrot_rec)
    for i, row in enumerate(x):
        for j, col in enumerate(y):
            grid[i, j] = vfunc(complex(row,col), 100)
    plt.gcf().set_facecolor("black")
    plt.imshow(grid.T, extent=(x.min(), x.max(), y.min(), y.max()), cmap='hot', origin='lower')


def vectorized_mandelbrot(c, I, z=0):
    pass


c_real = np.linspace(-2, 1, 1000)
c_imag = np.linspace(-1.5, 1.5, 1000)

c_r = c_real[np.newaxis, :]
c_i = c_imag[:, np.newaxis]

complex_grid = c_r + 1j*c_i

# draw_mandelbrot(c_real, c_imag)
# myb_optimized_draw_mandelbrot(c_real, c_imag)
# plt.show()