import numpy as np
import matplotlib.pyplot as plt
plt.figure(dpi = 1200)
filename = r"C:\Users\Dohyun\Downloads\4 (2)\iodine.csv"
x, y = np.loadtxt(filename, skiprows=2, delimiter= ",", usecols=(0,1), unpack=True)

local = []
for i in range(len(x)):
    if x[i] < 16000.0:
        pass
    elif x[i] < 20500.0:
        if y[i] > y[i - 1] and y[i] > y[i + 1]:
           if y[i - 1] > y[i - 2] or y[i + 1] > y[i + 2]:
                local.append(i)
                
x_local = []
y_local = []

for i in local:
    if (x[i] > 16000) and (x[i] < 20000):
        x_local.append(x[i])
        y_local.append(y[i])

plt.xlim([16500, 19500])


plt.scatter(x_local, y_local, color = 'forestgreen', s = 15)
plt.plot(x, y, color = 'royalblue', alpha = 0.75)
plt.title("Local maxima")
plt.show()


print(x_local)
