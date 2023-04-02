# -*- coding: utf-8 -*-
"""
Created on Sun Apr  2 23:29:11 2023

@author: Dohyun
"""

import numpy as np
from scipy.signal import find_peaks


#Data loading
x1, y1 = np.loadtxt(r'D:\4\chloroform s pole_QEP048921__0__17-18-50-433.txt', skiprows=14, usecols=(0,1), unpack=True)
x2, y2 = np.loadtxt(r'D:\4\chloroform p pole_2_QEP048921__0__17-20-20-441.txt', skiprows=14, usecols=(0,1), unpack=True)

peaks_1, _ = find_peaks(y1, height=40)
peaks_2, _ = find_peaks(y2, height=40)

possible_peak_1 = x1[peaks_1]
possible_peak_2 = x1[peaks_2]

peak_positions_1 = []
peak_positions_2 = []

x1 = list(x1)
y1 = list(y1)
data_1 = dict(zip(x1, y1))

x2 = list(x2)
y2 = list(y2)
data_2 = dict(zip(x2, y2))

#Peak fitting
last = 0 #Initialization

for i in range(len(possible_peak_1) - 1):
    if (possible_peak_1[i] - last) >= 1.5:
        peak_positions_1.append(possible_peak_1[i]) #Delete replicated peaks
        
        last = possible_peak_1[i]
        
last = 0 

for i in range(len(possible_peak_2) - 1):
    if (possible_peak_2[i] - last) >= 1.5:
        peak_positions_2.append(possible_peak_2[i]) #Delete replicated peaks
    
    last = possible_peak_2[i]

peak_positions_1.append(possible_peak_1[-1]) #Append last peak       
peak_positions_2.append(possible_peak_2[-1]) 

#Baseline and signal to noise ratio
base_1 = sum(y1[800:])/(len(y1) - 800)
base_2 = sum(y2[800:])/(len(y2) - 800)

peak_1_sn = []
peak_2_sn = []

for i in peak_positions_1:
    peak_1_sn.append(round(data_1[i] / base_1, 2))
for i in peak_positions_2:
    peak_2_sn.append(round(data_2[i] / base_2, 2))
    
#Data processing
report_peak = []
report_p_intensity = []
report_s_intensity = []
ratio = []

for i in range(len(peak_positions_1)):
    x = (peak_positions_1[i] + peak_positions_2[i])/2
    report_peak.append(round(x, 2))

for i in peak_positions_1:
    report_s_intensity.append(round(data_1[i], 2))

for i in peak_positions_2:
    print(data_2[i])
    report_p_intensity.append(round(data_2[i], 2))

for i in range(len(report_p_intensity)):
    x = report_s_intensity[i] / report_p_intensity[i]
    ratio.append(round(x, 2))

#Result section
print("p pole peaks:",peak_positions_2)
print("p pole SN ratio:",peak_2_sn)

print("=" * 80)

print("s pole peaks:", peak_positions_1)
print("s pole SN ratio:",peak_1_sn)

print("=" * 80)

print("Raman shift:", report_peak)
print("p pole intensity:", report_p_intensity)
print("s pole intensity:", report_s_intensity)
print("Polarization ratio:", ratio)

        