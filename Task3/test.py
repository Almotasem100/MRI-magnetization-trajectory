import cv2 as cv
import numpy as np
import math
import matplotlib as plt
from matplotlib import pyplot

import sympy as sp
def scos(x): return sp.N(sp.cos(x))
def ssin(x): return sp.N(sp.sin(x))


def open_Image():
    fname = "C:\\Users\\Al-Motasem\\OneDrive\\Desktop\\Task3\\test4.jpeg"
    if fname:
        imgPath = fname
        imgByte = cv.imread(imgPath)
        imgByte = cv.cvtColor(imgByte, cv.COLOR_BGR2GRAY)
        dimx, dimy = (imgByte.shape[0], imgByte.shape[1])
        # print("array", imgByte)
        # print("dim" , dimx, dimy)
        return imgByte

def create_phantom (image, T1w, T2w, T1o, T2o):
    phantom = [[[0] for i in range(16)] for j in range(16)]
    for x in range(16):
        for y in range(16):
            if(image[x][y] == 16):
                phantom[x][y] = [image[x][y], T1w, T2w]
            else:
                phantom[x][y] = [image[x][y], T1o, T2o]
    return phantom 
    # print(len(phantom))
    # print(phantom)


def rotating (vector , axis , angle):
    x, y, z = axis
    vector = np.array(vector)
    p1 = np.multiply(round(scos(sp.pi*angle/180)), [[1, 0, 0], [0, 1, 0], [0, 0, 1]])
    p2 = np.multiply(round((1-scos(sp.pi*angle/180))), [[x**2, x*y, x*z], [x*y, y**2, y*z], [x*z, y*z, z**2]])
    p3 = np.multiply(round(ssin(sp.pi*angle/180)), [[0, -z, y], [z, 0, -x], [-y, x, 0]])
    
    # print(np.cos(np.pi/2.))
    total = p1 + p2 + p3
    new_vector = np.dot(total, vector)
    return new_vector


image = open_Image()
phantom = create_phantom(image, 4, 2, 0.25 , 0.07)

vector_arr = [[[0, 0, 255] for i in range(16)] for j in range(16)]

K_space = [[0 for i in range(16)] for i in range(16)]

y_min = -45*sp.pi/180
y_max = 45*sp.pi/180
step = 90*sp.pi/(16*180)
summation = 0
for row in range(16):
    for col in range(16):
        vector_arr[row][col] = rotating(vector_arr[row][col], [0, 1, 0], 90)
        for row1 in range(16):
            y_gradient = row1 * abs(y_max - y_min)/16 - abs(y_max) 
            for col1 in range(16):
                x_gradient = col1 * (2*sp.pi)/16
                vector_arr[row1][col1][1] += y_gradient
                vector_arr[row1][col1][0] += x_gradient
                summation += np.abs(vector_arr[row1][col1]) * np.exp(-10/phantom[row1][col1][2])
        theta = x_gradient + y_gradient
        K_space[row][col] = summation * sp.cos(theta) + 1j * summation * sp.sin(theta)
        vector_arr = [[[0, 0, 255] for i in range(16)] for j in range(16)]
    y_max -= step
    y_min += step

print(K_space)
req_img = np.fft.ifft2(K_space)
print(req_img)
# plot_image = cv.cvtColor(req_img, cv.COLOR_BGR2GRAY)
req_img = np.log(np.abs(req_img))
image_plot = plt.pyplot.imshow(req_img)
plt.pyplot.show()
    

        






