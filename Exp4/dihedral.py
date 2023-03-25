# -*- coding: utf-8 -*-
"""
Created on Sat Mar 25 17:18:57 2023

@author: KOREA
"""

from matplotlib import pyplot as plt
import numpy as np
plt.figure(dpi = 1200)

x1, y1 = np.loadtxt(r'D:\matplot\2023_03_24_PChem4\ethane_tot_ener.txt', 
                    skiprows=4, usecols=(0,1), unpack=True)
plt.plot(x1, y1, color = "dimgray", label = 'Total Energy')

plt.xlabel("Dihedral angle", labelpad = 15, fontname = 'Arial', fontsize = 12, color = 'black', loc='center')
plt.ylabel("Total energy (Hatree)", labelpad = 10, fontname = 'Arial', fontsize = 12, color = 'black', loc='center')

plt.xticks(np.arange(0, 200, 20))
plt.xlim([0, 180])

plt.show()