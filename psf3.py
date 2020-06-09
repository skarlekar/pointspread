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


def mask_conv(img, kernel, mask):
    filtered = filters.convolve(img, kernel)
    return np.where(mask, filtered, img)


def blur(image, sigma, location, radius):

    # Generate a matrix with the same size as the input image. Fill it with value:False
    mask = np.zeros_like(image, dtype=np.bool)

    # Generate coordinates for a circle at a given location & radius
    y, x = location[0], location[1]
    cir = draw.circle(x, y, radius)

    # Wherever the circle is, replace the mask value to true
    mask[cir] = True

    # Apply gaussian blur on the whole image
    blurred = ndimage.gaussian_filter(image, sigma=sigma)

    # Apply the mask on the blurred image and get the blur only in the desired area
    out = np.where(mask, blurred, image)

    return out


def show(image, title):
    plt.imshow(image)
    plt.title(title)
    plt.show()


original = misc.face(gray=True)
show(original, "original")

location = (625, 450)
radius = 75
sigma = 3

blurred = blur(original, sigma, location, radius)
show(blurred, "final")


