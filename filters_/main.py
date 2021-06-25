import brightness
import emboss
import TV_60s
import tone
import sepia
import cv2
import pecil_drawing
import numpy as np


def kernel_generator(size):
    kernel = np.zeros((size, size), dtype=np.int8)
    for i in range(size):
        for j in range(size):
            if i < j:
                kernel[i][j] = 1
            elif i > j:
                kernel[i][j] = -1
    return kernel


def emboss1(img, size):
    height, width = img.shape[:2]
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    kernel = kernel_generator(size)  # generating kernel for bottom left kernel
    kernel = np.rot90(kernel, 1)  # switching kernel according to direction
    y = np.ones((height, width), np.uint8) * 128
    res = cv2.add(cv2.filter2D(gray, -1, kernel), y)

    cv2.imshow('Original', img)
    cv2.imwrite('tl.jpg', res)
    cv2.waitKey()


img = cv2.imread('./test_image/1.jpg')
# brightness.brightness(img)
emboss1(img, 3)
# TV_60s.tv_60(img)
# tone.tone(img)
# sepia.sepia(img)
# blend = pecil_drawing.pencil(img, 5)
# cv2.imshow('pencil', blend)
# cv2.waitKey()
