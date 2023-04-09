# -*- coding: utf-8 -*-
"""
Created on Sun Apr  9 21:36:40 2023

@author: Dohyun
"""

import matplotlib.pyplot as plt
import numpy as np
plt.figure(dpi = 1200)


#Data loading and blank correction
x1, y1 = np.loadtxt(r'C:\Users\Dohyun\Downloads\4 (1)\4\A.txt', skiprows=16, usecols=(1,2), unpack=True)
x2, y2 = np.loadtxt(r'C:\Users\Dohyun\Downloads\4 (1)\4\B.txt', skiprows=16, usecols=(1,2), unpack=True)
x3, y3 = np.loadtxt(r'C:\Users\Dohyun\Downloads\4 (1)\4\C.txt', skiprows=16, usecols=(1,2), unpack=True)
x4, y4 = np.loadtxt(r'C:\Users\Dohyun\Downloads\4 (1)\4\D.txt', skiprows=16, usecols=(1,2), unpack=True)

bx, by = np.loadtxt(r'C:\Users\Dohyun\Downloads\4 (1)\4\blank.txt', skiprows=16, usecols=(1,2), unpack=True)

y1 -= by
y2 -= by
y3 -= by
y4 -= by

#Plotting
plt.plot(x1, y1, color = 'brown', label = '0.0mM NaI')
plt.plot(x2, y2, color = 'darkorange', label = '6.0mM NaI')
plt.plot(x3, y3, color = 'forestgreen', label = '12.0mM NaI')
plt.plot(x4, y4, color = 'royalblue', label = '24.0mM NaI')

plt.legend(loc = 'best', ncol = 1, fontsize = 10, frameon = True, shadow = False)

plt.xlabel("Wavelength (nm)", labelpad = 15, fontname = 'Arial', fontsize = 12, color = 'black', loc='center')
plt.ylabel("Intensity (a.u.)", labelpad = 10, fontname = 'Arial', fontsize = 12, color = 'black', loc='center')

plt.title("Fluorescence spectrum of Rhodamine 6G", fontsize = 12)

plt.show()