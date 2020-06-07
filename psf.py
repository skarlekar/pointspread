from scipy import misc, ndimage
import matplotlib.pyplot as plt


class Error(Exception):
    pass


class InputError(Error):
    def __init__(self, message):
        self.message = message


def show(image):
    plt.imshow(image)
    plt.show()


def blur(image, sigma):
    return ndimage.gaussian_filter(image,sigma=sigma)


def crop(image, location, size):
    h, w = image.shape
    cx1, cy1 = location
    cx2 = cx1 + size[0]
    cy2 = cy1 + size[1]

    if (cx1 > w) or (cx2 > w):
        raise InputError("Width overflow")
    if (cy1 > h) or (cy2 > h):
        raise InputError("Height overflow")

    cropped_image = image[cy1:cy2, cx1:cx2]

    return cropped_image


def oldpaste(base, pasteable, location):
    h, w = pasteable.shape
    x, y = location[0], location[1]

    for i in range(x, x + w):
        for j in range(y, y + h):
            base[j, i] = pasteable[j - y, i - x]


def paste(base, pasteable, location):
    bh, bw = base.shape
    h, w = pasteable.shape
    x, y = location[0], location[1]

    if (x + w) > bw:
        raise InputError("Width overflow while performing paste operation")
    if (y + h) > bh:
        raise InputError("Height overflow while performing paste operation")

    base[y:y + h, x:x + w] = pasteable


original = misc.face(gray=True)
show(original)
print(original.shape)
location = (450, 275)
crop_size = (400, 200)
cropped = crop(original, location, crop_size)
show(cropped)

blurred_face = blur(cropped, 4)
show(blurred_face)
paste(original, blurred_face, location)
show(original)


