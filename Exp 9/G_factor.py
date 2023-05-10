import matplotlib.pyplot as plt
import numpy as np
plt.figure(dpi = 1200)

g_hh = np.loadtxt(r"C:\Users\Dohyun\Downloads\4 (3)\5-5 hh.txt", skiprows = 10)
g_hv = np.loadtxt(r"C:\Users\Dohyun\Downloads\4 (3)\5-5 hv.txt", skiprows = 10)

count = 0
avg = 0
for i in g_hh:
    if i < 100:
        count += 1
        avg += i
    else:
        break
avg/=count
g_hh -= avg

count = 0
avg = 0
for i in g_hv:
    if i < 100:
        count += 1
        avg += i
    else:
        break
avg/=count
g_hv -= avg


print("Max index is {}".format(np.argmax(g_hh)))

g_hh = g_hh[234:]
g_hv = g_hv[234:]
x = [0.0160 * i for i in range(len(g_hh))]

hh_area = hv_area = 0

for i, elem in enumerate(g_hh):
    hh_area += x[i] * g_hh[i]
    hv_area += x[i] * g_hv[i]
    
G = hv_area / hh_area
print("G factor is {}".format(G))


plt.plot(x, g_hh, color = 'forestgreen', label = 'HH')
plt.plot(x, g_hv, color = 'royalblue', label = 'HV')

plt.legend(loc = 'best', ncol = 1, fontsize = 10, frameon = True, shadow = False)

plt.xlabel("Time (ns)", labelpad = 10, fontname = 'Arial', fontsize = 12, color = 'black', loc='center')
plt.ylabel("Intensity", labelpad = 10, fontname = 'Arial', fontsize = 12, color = 'black', loc='center')
plt.show()