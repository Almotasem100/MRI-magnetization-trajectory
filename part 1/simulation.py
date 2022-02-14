import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import math

flag = True
flag2 = True
rotating_axis = [0,0,1]

def data_gen(num):
    global flag,flag2
    if flag2 is True:
        rotating_ang = num*np.pi/180
        rotating_ang2x = (3/2)*num*np.pi/180
        rotating_ang3x = (1/2)*num*np.pi/180
        if flag is True :    
            T1 = 200
            time = num
            M = (1-np.exp(-time/T1))
            pulse_ang = math.asin(M)
            print(pulse_ang)
        else:
            pulse_ang = 510*np.pi/(6*180)
        vector2 = [[3*np.exp(-num/120)*np.cos(rotating_ang)],[3*np.exp(-num/120)*np.sin(rotating_ang)],[0]]
    else:
        
        rotating_ang = 0
        pulse_ang = (85-(num-1440))*np.pi/180
        vector2 = [[3*np.cos(pulse_ang)*np.cos(rotating_ang)],[3*np.cos(pulse_ang)*np.sin(rotating_ang)],[0]]
    vector = [[3*np.cos(pulse_ang)*np.cos(rotating_ang)],[3*np.cos(pulse_ang)*np.sin(rotating_ang)],[3*np.sin(pulse_ang)]]
    vectorx = [[3*np.cos(pulse_ang)*np.cos(rotating_ang2x)],[3*np.cos(pulse_ang)*np.sin(rotating_ang2x)],[3*np.sin(pulse_ang)]]
    vectory = [[3*np.cos(pulse_ang)*np.cos(rotating_ang3x)],[3*np.cos(pulse_ang)*np.sin(rotating_ang3x)],[3*np.sin(pulse_ang)]] 
    vx, vy, vz = vector
    vxx, vyx, vzx = vectorx
    vxy, vyy, vzy = vectory
    vx2, vy2, vz2 = vector2
    ax.cla()
    ax.quiver(0, 0, 0, vx, vy, vz, pivot="tail", color="black", arrow_length_ratio=0.1)
    ax.quiver(0, 0, 0, vxx, vyx, vzx, pivot="tail", color="black", arrow_length_ratio=0.1)
    ax.quiver(0, 0, 0, vxy, vyy, vzy, pivot="tail", color="black", arrow_length_ratio=0.1)
    ax.quiver(0, 0, 0, vx2, vy2, vz2, pivot="tail", color="black",
            linestyle="dashed", arrow_length_ratio=0.1)
    if num == 1114:
        flag = False
    if num == 1439:
        flag2 = False
    p1 = []
    p2 = []
    p3 = []
    # p1x = []
    # p2x = []
    # p3x = []
    # p1y = []
    # p2y = []
    # p3y = []
    for i in range(0, 1114, 4):
        M_ = (1-np.exp(-i/200))
        pulse_ang2 = math.asin(M_)
        rotating_ang2 = i*np.pi/180
        # rotating_ang2y = 0.5*i*np.pi/180
        # rotating_ang3y = 1.5*i*np.pi/180
        p3.append(3*np.sin(pulse_ang2))
        p2.append(3*np.cos(pulse_ang2)*np.sin(rotating_ang2))
        p1.append(3*np.cos(pulse_ang2)*np.cos(rotating_ang2))
        # p3x.append(3*np.sin(pulse_ang2))
        # p2x.append(3*np.cos(pulse_ang2)*np.sin(rotating_ang2y))
        # p1x.append(3*np.cos(pulse_ang2)*np.cos(rotating_ang2y))
        # p3y.append(3*np.sin(pulse_ang2))
        # p2y.append(3*np.cos(pulse_ang2)*np.sin(rotating_ang3y))
        # p1y.append(3*np.cos(pulse_ang2)*np.cos(rotating_ang3y))

    #ax.scatter(p1, p2, p3, c='b')
    ax.plot(p1, p2, p3, c='b')
    # ax.plot(p1x, p2x, p3x, c='r')
    # ax.plot(p1y, p2y, p3y, c='g')
    ax.set_xlim(0,5)
    ax.set_ylim(0,5)
    ax.set_zlim(0,5)
    ax.view_init(elev=20., azim=32)
    x, y, z = np.zeros((3,3))
    u, v, w = np.array([[5,0,0],[0,5,0],[0,0,5]])
    ax.quiver(x,y,z,u,v,w,arrow_length_ratio=0.1)
    ax.view_init(elev=45, azim=190)
    if num == 0:
        flag = True
        flag2 = True
    
fig = plt.figure()
ax = fig.add_subplot(111,projection='3d')

data_gen(0)
ani = animation.FuncAnimation(fig, data_gen, range(1525), repeat = True, interval = 10)
plt.show()