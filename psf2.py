import numpy as np
import matplotlib.pyplot as plt
from scipy import signal


class Error(Exception):
    pass


class InputError(Error):
    def __init__(self, message):
        self.message = message


def generate_gaussian_kernel(size, sigma):
    a = np.linspace(-1, 1, size)
    b = np.linspace(-1, 1, size)
    x, y = np.meshgrid(a, b)
    d = np.sqrt(x * x + y * y)
    mu = 0.0
    g = np.exp(-((d - mu) ** 2 / (2.0 * sigma ** 2)))
    return g


def generate_gaussian_kernel_fast(size, sigma, normalised=False):
    '''
    Generates a n x n matrix with a centered gaussian
    of standard deviation std centered on it. If normalised,
    its volume equals 1.'''
    gaussian1D = signal.gaussian(size, sigma)
    gaussian2D = np.outer(gaussian1D, gaussian1D)
    if normalised:
        gaussian2D /= (2 * np.pi * (sigma ** 2))
    return gaussian2D

# a = np.linspace(-1, 1, 10)
# b = np.linspace(-1, 1, 10)
# x, y = np.meshgrid(a,b)
# d = np.sqrt(x*x+y*y)
# sigma, mu = 1.0, 0.0
# g = np.exp(-( (d-mu)**2 / ( 2.0 * sigma**2 ) ) )

gkern1 = generate_gaussian_kernel_fast(50, 1, False)
plt.imshow(gkern1, interpolation='none')
plt.title('gkern1')
plt.show()

gkern2 = generate_gaussian_kernel_fast(50, 2, False)
plt.imshow(gkern2, interpolation='none')
plt.title('gkern2')
plt.show()

gkern3 = generate_gaussian_kernel_fast(50, 3, False)
plt.imshow(gkern3, interpolation='none')
plt.title('gkern3')
plt.show()
