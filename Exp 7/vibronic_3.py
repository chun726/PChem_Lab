import matplotlib.pyplot as plt
import numpy as np

delta_g = [110.8, 105.3, 105.3, 105.2, 102.5, 108.0, 99.8, 99.7, 102.5, 102.5, 99.7, 91.4, 110.4, 86.3, 91.4, 88.7, 67.9, 85.9, 99.7, 80.3, 94.1, 74.8, 77.5, 72.1, 71.9, 69.3, 66.5, 66.5, 60.7, 61.2, 63.7, 52.6, 55.4, 52.6, 52.7, 49.8, 44.4, 44.3, 41.5, 41.6, 38.8]
v = [(i + 0.5) for i in range(5, 46)]

w = -1.8297113
b = 124.58274

c = 299792458 #m/s
m_eff = 1.0536491e-25 #kg

x = np.linspace(0, 50, 1000) 

plt.scatter(v, delta_g, color = 'forestgreen', s = 15)
plt.plot(x, w*x+b, color = 'royalblue')
plt.title("Regression")

plt.text(30, 100, r'$R^2$ = 0.924')
plt.text(30, 95, "y = -1.83 * x + 124.6")
plt.show()

v = b - 0.5 * w
x_e = (w / v) * -0.5
k = m_eff * (v *100 * 2 * np.pi * c) ** 2
v_d = -(b/w)
D_0 = 0.5 * v_d * b
D_e = D_0 + 0.5 * v - 0.25 * v * x_e

print("v~ =", v, "/cm")
print("x_e =", np.format_float_scientific(x_e, precision = 4, exp_digits = 1)) 
print("k =", k, "N/m")
print("v_d =", v_d, "/cm")
print("D_0 =", D_0, "/cm")
print("D_e =", D_e, "/cm")