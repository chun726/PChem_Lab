from scipy.optimize import curve_fit
import numpy as np
import matplotlib.pyplot as plt
plt.figure(dpi = 1200)

R1 = 100 #Ohm
R2 = 9.94
R3 = [22, 32, 37, 42, 47, 52, 62, 72]
Rf_Ri = [i/R2 for i in R3]

V_no_sample = [216, 304, 360, 416, 448, 488, 592, 672]
V_sample = [104, 144, 184, 200, 232, 256, 296, 352]

def linear(x, a, b):
    return a*x+b

def r_squared(y_true, y_pred):
    residual = y_true - y_pred
    ss_residual = np.sum(residual**2)
    ss_total = np.sum((y_true - np.mean(y_true))**2)
    r2 = 1 - (ss_residual / ss_total)
    return r2


popt, pconv = curve_fit(linear, Rf_Ri, V_no_sample)
a_no, b_no = popt
No_sample_fit = [a_no * i + b_no for i in Rf_Ri]
no_r2 = r_squared(np.array(V_no_sample), np.array(No_sample_fit))

popt, pconv = curve_fit(linear, Rf_Ri, V_sample)
a_sam, b_sam = popt
Sample_fit = [a_sam * i + b_sam for i in Rf_Ri]
sam_r2 = r_squared(np.array(V_sample), np.array(Sample_fit))

op = int(input("1-Without sample, 2-With sample : "))

if op == 1:
    plt.scatter(Rf_Ri, V_no_sample, color = "royalblue", label = "Without sample")
    plt.plot(Rf_Ri, No_sample_fit, color = "firebrick")
    plt.text(5, 350, "y = {}*x + {}".format(round(a_no, 4), round(b_no, 4)))
    plt.text(5, 325, r"R$^2$ = {}".format(round(no_r2, 4)))
elif op == 2:
    plt.scatter(Rf_Ri, V_sample, color = "forestgreen", label = "With sample")
    plt.plot(Rf_Ri, Sample_fit, color = "firebrick")
    plt.text(5, 150, "y = {}*x {}".format(round(a_sam, 4), round(b_sam, 4)))
    plt.text(5, 137, r"R$^2$ = {}".format(round(sam_r2, 4)))
    
plt.xlabel(r"${R_f}/{R_i}$")
plt.ylabel(r"${V_0}$ (mV)")
plt.legend(loc = "best")
plt.show()

I_0 = a_no / R1
I = a_sam / R1

print("Absorbance is {}".format(round(-np.log10(I/I_0), 4)))