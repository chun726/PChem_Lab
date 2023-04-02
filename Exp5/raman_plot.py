import matplotlib.pyplot as plt
import numpy as np
plt.figure(dpi = 1200)

x1, y1 = np.loadtxt(r'D:\4\chloroform s pole_QEP048921__0__17-18-50-433.txt', skiprows=14, usecols=(0,1), unpack=True)
x2, y2 = np.loadtxt(r'D:\4\chloroform p pole_2_QEP048921__0__17-20-20-441.txt', skiprows=14, usecols=(0,1), unpack=True)

plt.plot(x1, y1, color = 'brown', label = 's pole')
plt.plot(x2, y2, color = 'royalblue', label = 'p pole')

plt.xlim([530,700])
plt.ylim([0, 750])

plt.legend(loc = 'best', ncol = 1, fontsize = 10, frameon = True, shadow = False)

plt.xlabel(r"Raman shift (cm$^{-1}$)", labelpad = 15, fontname = 'Arial', fontsize = 12, color = 'black', loc='center')
plt.ylabel("Raman intensity (a.u)", labelpad = 10, fontname = 'Arial', fontsize = 12, color = 'black', loc='center')

plt.title(r"Raman scattering of CHCl$_3$", fontsize = 13)

plt.show()

