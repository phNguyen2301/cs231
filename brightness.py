import cv2
import numpy as np


def brightness(img ,factor):
    I = img.copy()
    intensitive_matrix = np.ones(img.shape, dtype=np.uint8) * abs(factor)
    if factor > 0:
        I = cv2.add(I, intensitive_matrix)
    elif factor < 0:
        I = cv2.subtract(I, intensitive_matrix)
    return I
