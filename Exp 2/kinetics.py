import csv
import matplotlib.pyplot as plt
import numpy as np
from itertools import islice
from scipy.optimize import curve_fit

x1 = []
y1 = []
x2 = []
y2 = []

with open(r"E:\test\THF_kinetics.csv", "r") as file:
    reader = csv.reader(file)
    row = list(reader)

skipped_rows_1 = islice(row, 2, len(row) - 33)

for row in skipped_rows_1:
    x1.append(float(row[0]))
    y1.append(float(row[1]))

with open(r"E:\test\cyclo_kinetics 3 (1).csv", "r") as file:
    reader = csv.reader(file)
    row = list(reader)
    
skipped_rows_2 = islice(row, 2, len(row) - 33)

for row in skipped_rows_2:
    x2.append(float(row[0]))
    y2.append(float(row[1]))
    
#=============================================#

print("1 - THF, 2 - Cyclohexane, 3 - THF short")
print("Choose: ", end = "")
op = int(input())

plt.figure(dpi = 1200)
plt.xlabel("Time (min)")
plt.ylabel("Abs")

for i, elem in enumerate(x1):
    if (y1[i] - y1[i+1]) > 0.03:
        start_1 = i + 1
        break
    
x1 = x1[start_1:]
y1 = y1[start_1:]
real_y1 = []

y_inf = y1[-1]
for i in y1:
    real_y1.append(np.log(y_inf - i))
    
for i in x1:
    if i > 5:
        begin = x1.index(i)
        break

x1 = x1[:begin]
y1 = y1[:begin]
real_y1 = real_y1[:begin]

x1_short = x1[:300]
real_y1_short = real_y1[:300]


for i, elem in enumerate(x2):
    if (y2[i] - y2[i+1]) > 0.03:
        start_2 = i + 1
        break
    
x2 = x2[start_2:]
y2 = y2[start_2:]
real_y2 = []

y_inf = y2[-1]
for i in y2:
    real_y2.append(np.log(y_inf - i))
    
for i in x2:
    if i > 25:
        begin = x2.index(i)
        break

x2 = x2[:begin]
y2 = y2[:begin]
real_y2 = real_y2[:begin]

#=============================================#

def linear(x, a, b):
    return a * x + b

def r_squared(y_true, y_pred):
    residual = y_true - y_pred
    ss_residual = np.sum(residual**2)
    ss_total = np.sum((y_true - np.mean(y_true))**2)
    r2 = 1 - (ss_residual / ss_total)
    return r2



popt, pconv = curve_fit(linear, x1 , real_y1)
a_thf, b_thf = popt
THF_fit = [b_thf + a_thf * i for i in x1]

popt, pconv = curve_fit(linear, x2 , real_y2)
a_cy, b_cy = popt
cy_fit = [b_cy + a_cy * i for i in x2]

popt, pconv = curve_fit(linear, x1_short, real_y1_short)
a_thf_short, b_thf_short = popt
THF_fit_short = [b_thf_short + a_thf_short * i for i in x1_short]

#=============================================#

if op == 1:
    plt.plot(x1, real_y1, color = "forestgreen", label = "THF")
    plt.plot(x1, THF_fit, color = "firebrick", label = "linear regression")
    plt.text(3, -3.4, "y = {}*x {}".format(round(a_thf, 4), round(b_thf, 4)))
    plt.text(3, -3.6,  r"R$^2$ = {}".format(round(r_squared(np.array(THF_fit), np.array(real_y1)), 4)))
    
elif op == 2:
    plt.plot(x2, real_y2, color = "royalblue", label = "Cyclohexane")
    plt.plot(x2, cy_fit, color = "firebrick", label = "linear regression")
    plt.text(5, -4.5, "y = {}*x {}".format(round(a_cy, 4), round(b_cy, 4)))
    plt.text(5, -4.7,  r"R$^2$ = {}".format(round(r_squared(np.array(cy_fit), np.array(real_y2)), 4)))

elif op == 3:
    plt.plot(x1_short, real_y1_short, color = "forestgreen")
    plt.plot(x1_short, THF_fit_short, color = "royalblue", label = "Short regression")
    plt.plot(x1[:300], THF_fit[:300], color = "firebrick", label = "Full regression")
    plt.text(1.1, -2.55, "y = {}*x {}".format(round(a_thf_short, 4), round(b_thf_short, 4)))
    plt.text(1.1, -2.58, r"R$^2$ = {}".format(round(r_squared(np.array(THF_fit_short), np.array(real_y1[:300])), 4)))
    

plt.legend(loc = "best")
plt.show()