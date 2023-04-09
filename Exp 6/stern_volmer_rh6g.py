# -*- coding: utf-8 -*-
"""
Created on Sun Apr  9 21:49:27 2023

@author: Dohyun
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks
plt.figure(dpi = 1200)

x1, y1 = np.loadtxt(r'C:\Users\Dohyun\Downloads\4 (1)\4\A.txt', skiprows=16, usecols=(1,2), unpack=True)
x2, y2 = np.loadtxt(r'C:\Users\Dohyun\Downloads\4 (1)\4\B.txt', skiprows=16, usecols=(1,2), unpack=True)
x3, y3 = np.loadtxt(r'C:\Users\Dohyun\Downloads\4 (1)\4\C.txt', skiprows=16, usecols=(1,2), unpack=True)
x4, y4 = np.loadtxt(r'C:\Users\Dohyun\Downloads\4 (1)\4\D.txt', skiprows=16, usecols=(1,2), unpack=True)

bx, by = np.loadtxt(r'C:\Users\Dohyun\Downloads\4 (1)\4\blank.txt', skiprows=16, usecols=(1,2), unpack=True)

y1 -= by
y2 -= by
y3 -= by
y4 -= by


x = 80
y = 250
largest_area = [0, 0, 0, 0]
index_num = [0, 0, 0, 0]
largest_point = []

peaks, _ = find_peaks(y1, height = 2000)
for i in peaks:
    area = np.trapz(y1[i-x:i+y], x1[i-x:i+y])
    if area > largest_area[0]:
        largest_area[0] = area
        index_num[0] = i

peaks, _ = find_peaks(y2, height = 2000)
for i in peaks:
    area = np.trapz(y2[i-x:i+y], x2[i-x:i+y])
    if area > largest_area[1]:
        largest_area[1] = area
        index_num[1] = i
        
peaks, _ = find_peaks(y3, height = 2000)
for i in peaks:
    area = np.trapz(y3[i-x:i+y], x3[i-x:i+y])
    if area > largest_area[2]:
        largest_area[2] = area
        index_num[2] = i
        
peaks, _ = find_peaks(y4, height = 2000)
for i in peaks:
    area = np.trapz(y4[i-x:i+y], x4[i-x:i+y])
    if area > largest_area[3]:
        largest_area[3] = area
        index_num[3] = i

largest_point.append(x1[index_num[0]])
largest_point.append(x2[index_num[1]])
largest_point.append(x3[index_num[2]])
largest_point.append(x4[index_num[3]])

plt.plot(x1, y1)
plt.plot([x1[index_num[0] - x], x1[index_num[0] + y]], [y1[index_num[0] - x], y1[index_num[0] + y]])

plt.plot(x2, y2)
plt.plot([x2[index_num[1] - x], x2[index_num[1] + y]], [y2[index_num[1] - x], y2[index_num[1] + y]])

plt.plot(x3, y3)
plt.plot([x3[index_num[2] - x], x3[index_num[2] + y]], [y3[index_num[2] - x], y3[index_num[2] + y]])

plt.plot(x4, y4)
plt.plot([x4[index_num[3] - x], x4[index_num[3] + y]], [y4[index_num[3] - x], y4[index_num[3] + y]])

print("Area of fluorosence peak is", largest_area)
print("Maximum point is", largest_point)

plt.show()