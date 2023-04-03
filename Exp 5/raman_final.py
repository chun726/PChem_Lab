# -*- coding: utf-8 -*-
"""
Created on Mon Apr  3 23:57:09 2023

@author: Dohyun
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks

plt.figure(dpi = 1200)

x1, y1 = np.loadtxt(r'D:\4\chloroform s pole_QEP048921__0__17-18-50-433.txt', skiprows=50, usecols=(0,1), unpack=True)
x2, y2 = np.loadtxt(r'D:\4\chloroform p pole_2_QEP048921__0__17-20-20-441.txt', skiprows=50, usecols=(0,1), unpack=True)

x1 = (1e7/532) - (1e7/x1)
x2 = (1e7/532) - (1e7/x2)

plt.xlim([0,3500])
plt.ylim([0, 600])

plt.plot(x1, y1, color = 'brown', label = 's pole')
plt.plot(x2, y2, color = 'royalblue', label = 'p pole')

plt.legend(loc = 'best', ncol = 1, fontsize = 10, frameon = True, shadow = False)

plt.xlabel(r"Raman shift (cm$^{-1}$)", labelpad = 15, fontname = 'Arial', fontsize = 12, color = 'black', loc='center')
plt.ylabel("Raman intensity (a.u)", labelpad = 10, fontname = 'Arial', fontsize = 12, color = 'black', loc='center')

plt.title(r"Raman scattering of CHCl$_3$", fontsize = 13)

plt.show()

temp_peaks_1, _ = find_peaks(y1, height=40)
temp_peaks_2, _ = find_peaks(y2, height=40)

possible_peak_1 = x1[temp_peaks_1]
possible_peak_2 = x1[temp_peaks_2]

peak_1 = [possible_peak_1[0]]
peak_2 = [possible_peak_2[0]]

for i in range(1, len(possible_peak_1)):
    if abs(possible_peak_1[i] - possible_peak_1[i-1]) >= 25:
        peak_1.append(possible_peak_1[i])
        
for i in range(1, len(possible_peak_2)):
    if abs(possible_peak_2[i] - possible_peak_2[i-1]) >= 25:
        peak_2.append(possible_peak_2[i])

true_peak = []
for i in range(len(peak_1)):
    x = (peak_1[i] + peak_2[i])/2
    true_peak.append(round(x, 2))

x1 = list(x1)
y1 = list(y1)
data_1 = dict(zip(x1, y1))

x2 = list(x2)
y2 = list(y2)
data_2 = dict(zip(x2, y2))

p_intensity = []
for i in peak_2:
    p_intensity.append(data_2[i])
    
s_intensity = []
for i in peak_1:
    s_intensity.append(data_1[i])

ratio = []
for i in range(len(p_intensity)):
    x = s_intensity[i]/p_intensity[i]
    ratio.append(round(x, 2))
    
#Result section
print("Raman Shift:", true_peak)
print("p pole intensity:", p_intensity)
print("s pole intensity:", s_intensity)
print("Polarization ratio:", ratio)

