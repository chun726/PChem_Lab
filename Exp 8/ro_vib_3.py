

import matplotlib.pyplot as plt
import numpy as np
plt.figure(dpi = 1200)

x1, y1 = np.loadtxt(r'D:\4\HCl DCl.csv', skiprows=5, usecols=(0,1), unpack=True, delimiter = ",")

state = True
sum_left = 0
sum_right = 0

for i in range(len(x1)):
    if x1[i] > 2830.0 and x1[i] < 2850.0:
        dx = x1[i] - x1[i - 1]
        
        if y1[i-1] > y1[i] and y1[i+1] > y1[i]:
            t = i
            
        if state == True and y1[i] > 0.2:
            t1 = i
            state = False
        if state == False and y1[i] < 0.2:
            t2 = i
            state = True
        
for i in range(t1, t2 +1):
    if i <= t:
        sum_left += (dx * y1[i])
    if i >= t:
        sum_right += (dx * y1[i])

sum_left /= sum_right
sum_right /= sum_right
sum_left = round(sum_left, 2)

plt.plot(x1, y1, label = "Absorbance", linewidth = .7)
plt.scatter(x1[t], y1[t], s = 15, color = "Forestgreen")
plt.scatter(x1[t1], y1[t1], s = 15, color = "maroon")
plt.scatter(x1[t2], y1[t2], s = 15, color = "Darkorange")

plt.vlines(x1[t], -1, y1[t], color = "Forestgreen", linestyles = "dashed")
plt.vlines(x1[t1], -1, y1[t1], color = "rosybrown", linestyles = "dashed")
plt.vlines(x1[t2], -1, y1[t2], color = "Darkorange", linestyles = "dashed")

plt.fill_between(x1[t1:t+1], y1[t1:t+1], alpha = 0.5, color = "maroon")
plt.fill_between(x1[t:t2+1], y1[t:t2+1], alpha = 0.5, color = "Darkorange")

plt.text(2840.0, 0.3, r"$H^{37}$Cl")
plt.text(2842.5, 0.3, r"$H^{35}$Cl")
plt.text(2839.12, 0.2, f"Area ratio = {sum_left}:{sum_right}")


plt.xlabel(r"Wavenumber (cm$^{-1}$)", labelpad = 15, fontname = 'Arial', fontsize = 12, color = 'black', loc='center')
plt.ylabel("Intensity (a.u)", labelpad = 10, fontname = 'Arial', fontsize = 12, color = 'black', loc='center')

plt.legend(loc = 'best')

plt.title("Rotation - vibration spectrum")

plt.xlim([2830, 2850])
plt.ylim([0, 1.5])
plt.show()