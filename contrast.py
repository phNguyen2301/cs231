import cv2
import numpy as np

def contrast(img, factor ,mid= 0.5):
    I = img.copy()
    #constrast : do tuong phan
    #Adjust the contrast by increasing the difference from the user-defined midpoint by some amount, factor
    #So basically, what we need to do is make the bigger difference to the midpoint
    x_pixels = I.shape[0]
    y_pixels = I.shape[1]
    num_channel = I.shape[2]
    for x in range(x_pixels):
        for y in range(y_pixels):
            for z in range(num_channel):
                I[x,y,z] = (I[x,y,z])*factor + mid

    return I