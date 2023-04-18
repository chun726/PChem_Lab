import matplotlib.pyplot as plt
import numpy as np
plt.figure(dpi = 1200)

x1, y1 = np.loadtxt(r'C:\Users\Dohyun\Downloads\4 (2)\iodine.csv', skiprows=2, delimiter= ",", usecols=(0,1), unpack=True)

plt.plot(x1, y1, color = 'dimgray', label = 'vibronic spectrum', alpha = 1.0)


plt.xlim([15500, 20500])
#plt.ylim([0, 750])

plt.legend(loc = 'best', ncol = 1, fontsize = 10, frameon = True, shadow = False)

plt.xlabel(r"Wavenumber (cm$^{-1}$)", labelpad = 15, fontname = 'Arial', fontsize = 12, color = 'black', loc='center')
plt.ylabel("Absorbance", labelpad = 10, fontname = 'Arial', fontsize = 12, color = 'black', loc='center')

plt.title(r"Vibronic spectrum of I$_2$", fontsize = 13)

plt.show()