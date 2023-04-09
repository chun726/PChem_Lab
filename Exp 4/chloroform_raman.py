# -*- coding: utf-8 -*-
"""
Created on Sat Mar 25 17:33:50 2023

@author: KOREA
"""

from matplotlib import pyplot as plt
import numpy as np
plt.figure(dpi = 1200)

x1, y1 = np.loadtxt(r'D:\matplot\2023_03_24_PChem4\chloroform_raman_act.txt', 
                    skiprows=18, usecols=(0,1), unpack=True)
plt.plot(x1, y1, color = "dimgray", label = 'Total Energy')

plt.xlabel(r"Frequency ($cm^{-1}$)", labelpad = 15, fontname = 'Arial', fontsize = 12, color = 'black', loc='center')
plt.ylabel(r"Intensity", labelpad = 10, fontname = 'Arial', fontsize = 12, color = 'black', loc='center')

plt.title("Raman Activity Spectrum")

plt.show()
