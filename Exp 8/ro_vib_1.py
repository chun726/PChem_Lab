# -*- coding: utf-8 -*-
"""
Created on Fri Apr 28 18:56:17 2023

@author: Dohyun
"""

import matplotlib.pyplot as plt
import numpy as np
plt.figure(dpi = 1200)

x1, y1 = np.loadtxt(r'D:\4\HCl DCl.csv', skiprows=5, usecols=(0,1), unpack=True, delimiter = ",")

plt.plot(x1, y1, label = "Absorbance", linewidth = .7)

plt.xlabel(r"Wavenumber (cm$^{-1}$)", labelpad = 15, fontname = 'Arial', fontsize = 12, color = 'black', loc='center')
plt.ylabel("Intensity (a.u)", labelpad = 10, fontname = 'Arial', fontsize = 12, color = 'black', loc='center')

plt.legend(loc = 'best')

plt.title("Rotation - vibration spectrum")

plt.xlim([1800, 3300])

plt.show()