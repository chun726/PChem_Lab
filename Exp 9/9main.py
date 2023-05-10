import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
plt.figure(dpi = 1200)

G = 0.7896332068077502
vh_37 = np.loadtxt(r"C:\Users\Dohyun\Downloads\4 (3)\3-7 vh.txt", skiprows = 10) * G #I_vertical
vv_37 = np.loadtxt(r"C:\Users\Dohyun\Downloads\4 (3)\3-7 vv.txt", skiprows = 10) #I_perpendicular
vh_46 = np.loadtxt(r"C:\Users\Dohyun\Downloads\4 (3)\4-6 vh.txt", skiprows = 10) * G #I_vertical
vv_46 = np.loadtxt(r"C:\Users\Dohyun\Downloads\4 (3)\4-6 vv.txt", skiprows = 10) #I_perpendicular
vh_55 = np.loadtxt(r"C:\Users\Dohyun\Downloads\4 (3)\5-5 vh.txt", skiprows = 10) * G #I_vertical
vv_55 = np.loadtxt(r"C:\Users\Dohyun\Downloads\4 (3)\5-5 vv.txt", skiprows = 10) #I_perpendicular
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

count = 0
avg = 0
for i in vh_46:
    if i < 100:
        count += 1
        avg += i
    else:
        break
avg/=count
vh_46 -= avg

count = 0
avg = 0
for i in vv_46:
    if i < 100:
        count += 1
        avg += i
    else:
        break
avg/=count
vv_46 -= avg

count = 0
avg = 0
for i in vh_55:
    if i < 100:
        count += 1
        avg += i
    else:
        break
avg/=count
vh_55 -= avg

count = 0
avg = 0
for i in vv_55:
    if i < 100:
        count += 1
        avg += i
    else:
        break
avg/=count
vv_55 -= avg

#=====================================================#
#=====================Variable========================#
#=====================================================#

xa = 200
ya = 400
xb = 230

P_37 = (vv_37 + 2 * vh_37) / 3
P_37 = P_37[xb:]
r_37 = (vv_37 - vh_37) / (vv_37 + 2 * vh_37)
r_37 = r_37[xa:ya]

P_46 = (vv_46 + 2 * vh_46) / 3
P_46 = P_46[xb:]
r_46 = (vv_46 - vh_46) / (vv_46 + 2 * vh_46)
r_46 = r_46[xa:ya]

P_55 = (vv_55 + 2 * vh_55) / 3
P_55 = P_55[xb:]
r_55 = (vv_55 - vh_55) / (vv_55 + 2 * vh_55)
r_55 = r_55[xa:ya]

#=====================================================#
#====================Regression=======================#
#=====================================================#
def exponential(x, a, b, c):
    return a * np.exp(-b * x) + c

def r_squared(y_true, y_pred):
    residual = y_true - y_pred
    ss_residual = np.sum(residual**2)
    ss_total = np.sum((y_true - np.mean(y_true))**2)
    r2 = 1 - (ss_residual / ss_total)
    return r2


popt_37, pcov = curve_fit(exponential, x[xb:], P_37)
a_37, b_37, c_37 = popt_37

popt_46, pcov = curve_fit(exponential, x[xb:], P_46)
a_46, b_46, c_46 = popt_46

popt_55, pcov = curve_fit(exponential, x[xb:], P_55)
a_55, b_55, c_55 = popt_55

ropt_37, pcov = curve_fit(exponential, x[xa:ya], r_37)
d_37, e_37, f_37 = ropt_37

ropt_46, pcov = curve_fit(exponential, x[xa:ya], r_46)
d_46, e_46, f_46 = ropt_46

ropt_55, pcov = curve_fit(exponential, x[xa:ya], r_55)
d_55, e_55, f_55 = ropt_55
#=====================================================#
#=====================Plotting========================#
#=====================================================#
t = np.linspace(0, 100, 100000)



r_55_fit = [f_55 + d_55 * np.exp(-e_55 * i) for i in x[xa:ya]]
r2_55 = r_squared(r_55, r_55_fit)

r_46_fit = [f_46 + d_46 * np.exp(-e_46 * i) for i in x[xa:ya]]
r2_46 = r_squared(r_46, r_46_fit)

r_37_fit = [f_37 + d_37 * np.exp(-e_37 * i) for i in x[xa:ya]]
r2_37 = r_squared(r_37, r_37_fit)

plt.plot(x[xa:ya], r_55, color = 'forestgreen', label = '5:5')
plt.plot(t, exponential(t, *ropt_55), color = "darkgreen")
plt.text(4.0, 0.26, "y = {} * exp(-{}x) {}, R$^{}$ = {}".format(round(d_55, 2), round(e_55, 2), round(f_55, 2), 2, round(r2_55, 2)), color = "darkgreen", size = 9)

plt.plot(x[xa:ya], r_46, color = 'royalblue', label = '4:6')
plt.plot(t, exponential(t, *ropt_46), color = "navy")
plt.text(4.0, 0.24, "y = {} * exp(-{}x) + {}, R$^{}$ = {}".format(round(d_46, 2), round(e_46, 2), round(f_46, 2), 2, round(r2_46, 2)), color = "navy", size = 9)

plt.plot(x[xa:ya], r_37, color = 'salmon', label = '3:7')
plt.plot(t, exponential(t, *ropt_37), color = "brown")
plt.text(4.0, 0.22, "y = {} * exp(-{}x) {}, R$^{}$ = {}".format(round(d_37, 2), round(e_37, 2), round(f_37, 2), 2, round(r2_37, 2)), color = "brown", size = 9)


plt.legend(loc = 'best', ncol = 1, fontsize = 10, frameon = True, shadow = False)

plt.xlabel("Time (ns)", labelpad = 10, fontname = 'Arial', fontsize = 12, color = 'black', loc='center')
plt.ylabel("Intensity", labelpad = 10, fontname = 'Arial', fontsize = 12, color = 'black', loc='center')

plt.xlim(3, 7)
plt.ylim(0, 0.3)

plt.show()

#============Another one=============#

plt.figure(dpi = 1200)
xp = x[xb:]

p_55_fit = [c_55 + a_55 * np.exp(-b_55 * i) for i in x[xb:]]
p2_55 = r_squared(P_55, p_55_fit)

p_46_fit = [c_46 + a_46 * np.exp(-b_46 * i) for i in x[xb:]]
p2_46 = r_squared(P_46, p_46_fit)

p_37_fit = [c_37 + a_37 * np.exp(-b_37 * i) for i in x[xb:]]
p2_37 = r_squared(P_37, p_37_fit)

plt.plot(xp, P_55, color = 'forestgreen', label = '5:5')
plt.plot(t, exponential(t, *popt_55), color = "darkgreen")
plt.text(8, 4000, r"y = {} * exp(-{}x) {}, R$^{}$ = {}".format(round(a_55, 2), round(b_55, 2), round(c_55, 2), 2, round(p2_55, 2)), color = "darkgreen", size = 9)


plt.plot(xp, P_46, color = 'royalblue', label = '4:6')
plt.plot(t, exponential(t, *popt_46), color = "navy")
plt.text(8, 3500, r"y = {} * exp(-{}x) {}, R$^{}$ = {}".format(round(a_46, 2), round(b_46, 2), round(c_46, 2), 2, round(p2_46, 2)), color = "navy", size = 9)

plt.plot(xp, P_37, color = 'salmon', label = '3:7')
plt.plot(t, exponential(t, *popt_37), color = "brown")
plt.text(8, 3000, r"y = {} * exp(-{}x) {}, R$^{}$ = {}".format(round(a_37, 2), round(b_37, 2), round(c_37, 2), 2, round(p2_37, 2)), color = "brown", size = 9)

plt.legend(loc = 'best', ncol = 1, fontsize = 10, frameon = True, shadow = False)

plt.xlabel("Time (ns)", labelpad = 10, fontname = 'Arial', fontsize = 12, color = 'black', loc='center')
plt.ylabel("Intensity", labelpad = 10, fontname = 'Arial', fontsize = 12, color = 'black', loc='center')

plt.xlim([3, 16])
plt.ylim([0, 6000])
plt.xticks(ticks = [i for i in range(4, 17)])

plt.show()

print(1/b_55)
print(1/b_46)
print(1/b_37)

