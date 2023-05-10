import matplotlib.pyplot as plt
import numpy as np
plt.figure(dpi = 1200)

vh_37 = np.loadtxt(r"C:\Users\Dohyun\Downloads\4 (3)\3-7 vh.txt", skiprows = 10)
vv_37 = np.loadtxt(r"C:\Users\Dohyun\Downloads\4 (3)\3-7 vv.txt", skiprows = 10)
x = [0.0160 * i for i in range(len(vv_37))]

count = 0
avg = 0
for i in vh_37:
    if i < 100:
        count += 1
        avg += i
    else:
        break
avg/=count
vh_37 -= avg

count = 0
avg = 0
for i in vv_37:
    if i < 100:
        count += 1
        avg += i
    else:
        break
avg/=count
vv_37 -= avg

plt.plot(x, vh_37, color = 'forestgreen', label = "VH")
plt.plot(x, vv_37, color = 'royalblue', label = "VV")

plt.legend(loc = 'best', ncol = 1, fontsize = 10, frameon = True, shadow = False)

plt.title("Before G-factor calibration - 3:7")

plt.xlabel("Time (ns)", labelpad = 10, fontname = 'Arial', fontsize = 12, color = 'black', loc='center')
plt.ylabel("Intensity", labelpad = 10, fontname = 'Arial', fontsize = 12, color = 'black', loc='center')

plt.show()

vh_37 *= 0.7896332068077502
plt.figure(dpi = 1200)
plt.plot(x, vh_37, color = 'forestgreen', label = "VH")
plt.plot(x, vv_37, color = 'royalblue', label = "VV")

plt.legend(loc = 'best', ncol = 1, fontsize = 10, frameon = True, shadow = False)

plt.title("after G-factor calibration - 3:7")

plt.xlabel("Time (ns)", labelpad = 10, fontname = 'Arial', fontsize = 12, color = 'black', loc='center')
plt.ylabel("Intensity", labelpad = 10, fontname = 'Arial', fontsize = 12, color = 'black', loc='center')

plt.show()