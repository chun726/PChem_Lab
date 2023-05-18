import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

plt.figure(dpi = 1200)

mM = [1.0, 4.0, 10.0, 20.0, 100.0]
NaCl = [106.7, 441, 1061, 2080, 5130]
AcOH  = [51.2, 101.3, 155.9, 214, 468]
AcOH_S = AcOH.copy()

for i, elem in enumerate(mM):
    NaCl[i] /= elem
    AcOH[i] /= elem
    
#=================================#
#============Fig 1================#
#=================================#
#plt.scatter(mM, NaCl, color = "forestgreen", label = "NaCl")
#plt.scatter(mM, AcOH, color = "royalblue", label = "AcOH")
#plt.legend(loc = 'best')

#plt.xlabel("molar concentration (mM)")
#plt.ylabel(r"molar conductivity ($\frac{{\mu}S}{cm * mM}$)")


def root(x, a, b):
    return b - a * np.sqrt(x)

def linear(x, a, b):
    return a * x + b

def r_squared(y_true, y_pred):
    residual = y_true - y_pred
    ss_residual = np.sum(residual**2)
    ss_total = np.sum((y_true - np.mean(y_true))**2)
    r2 = 1 - (ss_residual / ss_total)
    return r2

AcOH_I = []

for i in range(5):
    AcOH_I.append(1/AcOH[i])
    
popt, pconv = curve_fit(root, mM, NaCl)
a_nacl, b_nacl = popt
NaCl_fit = [b_nacl - a_nacl * np.sqrt(i) for i in mM]


popt_2, pconv_2 = curve_fit(linear, AcOH_S, AcOH_I)
a_acoh, b_acoh = popt_2
AcOH_fit = [b_acoh + a_acoh * i for i in AcOH_S]

t = np.arange(0, 500, 0.1)

#=================================#
#============Fig 2.1==============#
#=================================#
#plt.plot(t, b_nacl - a_nacl * np.sqrt(t), color = "forestgreen", label = "Experimental plot")
#plt.plot(t, 126.45 - 2.1 * np.sqrt(t), color = "firebrick", label = "True plot")
#plt.scatter(mM, NaCl, color = "Darkgreen")


#plt.xlabel("molar concentration (mM)")
#plt.ylabel(r"molar conductivity ($\frac{{\mu}S}{cm * mM}$)")

#plt.text(60, 100, "y = {} - {}*{}".format(round(b_nacl, 2), round(a_nacl, 2), r"$\sqrt{x}$"))
#plt.text(60, 95, r"R$^2$ = {}".format(round(r_squared(np.array(NaCl), np.array(NaCl_fit)), 6)))
#plt.title("NaCl's Kohlausch's law plot")

#plt.xlim([0, 110])
#plt.ylim([50, 130])

#plt.legend(loc = "best")
#=================================#
#============Fig 2.2==============#
#=================================#
plt.plot(t, a_acoh * t + b_acoh, color = "royalblue", label = "Experimental plot")
plt.plot(t,  0.000377*t+ 0.00256, color = "firebrick", label = "True plot")
plt.scatter(AcOH_S, AcOH_I, color = "darkblue")


plt.xlabel(r"conductivity (${\mu}$S/cm)")
plt.ylabel(r"1/(molar conductivity) ($\frac{cm * mM}{{\mu}S}$)")

plt.legend(loc = "best")

plt.text(300, 0.05, "y = {}*x {}".format(round(a_acoh, 6), round(b_acoh, 6)))
plt.text(300, 0.035, r"R$^2$ = {}".format(round(r_squared(np.array(AcOH_I), np.array(AcOH_fit)), 6)))
plt.title("AcOH's Oswald's dilution law plot")

plt.xlim([0, 500])
plt.show()


