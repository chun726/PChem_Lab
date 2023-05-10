import numpy as np
import matplotlib.pyplot as plt

plt.figure(dpi = 1200)

wt = [1.31, 2.52, 3.74, 6.16, 9.18, 12.21, 15.23, 18.26]
glycerol = [0.971, 0.967, 0.953, 0.931, 0.902, 0.873, 0.844, 0.815]

lst = np.polyfit(wt, glycerol, 1)



x = np.linspace(0, 20, 10000)
plt.scatter(wt, glycerol, color = 'forestgreen', label = "Glycerol, 25℃")
plt.plot(x, lst[0] * x + lst[1], color = "Darkgreen" )

plt.text(12.5, 0.925, "f(x) = {}x + {}".format(round(lst[0], 3), round(lst[1], 3)), color = "Darkgreen")
plt.text(12.5, 0.910, "f(100) = {}".format(round(100*lst[0] + lst[1], 3)), color = "Darkgreen")
plt.legend(loc = 'best')

plt.xlabel("Weight percent (%)")
plt.ylabel(r"Relative solubility $\alpha_i$ / $\alpha_0$")
plt.show()
