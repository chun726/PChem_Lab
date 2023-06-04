import matplotlib.pyplot as plt
import numpy as np
plt.figure(dpi = 1200)

R3 = [22, 32, 37, 42, 47, 52, 62, 72]
V_sample = [104, 144, 184, 200, 232, 256, 296, 352]
V_no_sample = [216, 304, 360, 416, 448, 488, 592, 672]

Transmittance = []

for i, elem in enumerate(R3):
    I = V_sample[i] / (R3[i] * 100)
    I0 = V_no_sample[i] / (R3[i] * 100)
    
    t = -np.log10(I/I0)
    Transmittance.append(t)

avg = sum(Transmittance) / len(Transmittance)

print(Transmittance)


plt.scatter(R3, Transmittance, color = "forestgreen")
plt.plot(np.linspace(20, 80, 100), [avg for i in range(100)], color = "firebrick", label = "average")

plt.xlabel(r"${R_f}$ (k$\Omega$)")
plt.ylabel("Absorbance")

plt.legend(loc = "best")
plt.xlim([20, 75])