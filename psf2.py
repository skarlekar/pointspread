import numpy as np
import matplotlib.pyplot as plt
from scipy import signal, misc, ndimage
from scipy.ndimage import filters
from skimage import draw
import matplotlib.pyplot as plt


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


def mask_conv(img, kernel, mask):
    filtered = filters.convolve(img, kernel)
    return np.where(mask, filtered, img)


def blur(image, kernel_size, sigma, location, radius):

    # Generate a matrix with the same size as the input image. Fill it with value:False
    mask = np.zeros_like(image, dtype=np.bool)

    # Generate coordinates for a circle at a given location & radius
    y, x = location[0], location[1]
    cir = draw.circle(x, y, radius)

    # Wherever the circle is, replace the mask value to true
    mask[cir] = True

    # Generate a kernel with the given size & standard deviation
    kernel = generate_gaussian_kernel_fast(kernel_size, sigma, True)

    # Convolve the kernel over the image through the mask
    # only the areas set to true will be convolved
    out = mask_conv(image, kernel, mask)

    return out


def show(image):
    plt.imshow(image)
    plt.show()


original = misc.face(gray=True)
show(original)

kernel_size = 3
location = (625, 450)
radius = 75
sigma = 1

blurred = blur(original, kernel_size, sigma, location, radius)
show(blurred)


