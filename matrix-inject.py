import numpy as np


class Error(Exception):
    pass


class InputError(Error):
    def __init__(self, message):
        self.message = message


def paste(base, pasteable, location):
    bh, bw = base.shape
    h, w = pasteable.shape
    x, y = location[0], location[1]

    if (x+w) > bw:
        raise InputError("Width overflow while performing paste operation")

    if (y+h) > bh:
        raise InputError("Height overflow while performing paste operation")

    base[y:y+h, x:x+w] = pasteable


arr1 = np.ones((5, 5))
print(arr1)

arr2 = np.random.randint(100, size=(3, 2))
print(arr2)

loc = (3, 2)
paste(arr1, arr2, loc)
print(arr1)

# arr1[3:5, 3:5] = arr2

