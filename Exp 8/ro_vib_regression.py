import matplotlib.pyplot as plt

D_P = [0, 2079.869826, 2068.781043, 2057.692261, 2046.121358, 2034.550455, 2022.738492, 2010.685468, 
          1998.391383, 1985.856238, 1973.321093, 1960.54488, 1947.527622, 1934.269295]

D_R = [2101.324208, 2111.448748, 2121.573289, 2131.456768, 2141.099188, 2150.500546, 2159.660845, 
          2168.580082, 2177.258260, 2185.695376, 2193.650672, 2201.605368, 2209.319304, 2216.551118]


H_P = [0, 2864.280629, 2842.585186, 2820.407622, 2797.988997, 2774.847191, 2751.464324, 2727.117216, 
          2702.529047, 2677.217696, 2651.424225, 2625.389693]

H_R = [2905.501971, 2925.02787, 2943.830588, 2962.392245, 2980.23072, 2997.346014, 3013.738127, 
          3029.407058, 3044.593868, 3058.816437, 3072.315824, 3085.922485]

J_H_ground = [(i**2 + i + 1) for i in range(1, 11)]
H_ground = []

J_H_excited = [(i**2 + i + 1) for i in range(1, 12)]
H_excited = []

J_D_ground = [(i**2 + i + 1) for i in range(1, 13)]
D_ground = []

J_D_excited = [(i**2 + i + 1) for i in range(1, 14)]
D_excited = []

for i in range(1, 11):
    t = (H_R[i - 1] - H_P[i + 1])/(i + 1/2)
    H_ground.append(t)

for i in range(1, 12):
    t = (H_R[i] - H_P[i]) / (i + 1/2)
    H_excited.append(t)

for i in range(1, 13):
    t = (D_R[i - 1] - D_P[i + 1]) / (i + 1/2)
    D_ground.append(t)

for i in range(1, 14):
    t = (D_R[i] - D_P[i]) / (i + 1/2)
    D_excited.append(t)

fig, ax1 = plt.subplots()
ax2 = ax1.twinx()

ax1.scatter([], [], color = "Navy", s = 10, label=r"$D^{35}Cl$ $\nu=1$")
ax1.scatter(J_D_ground, D_ground, s = 10, color = "Forestgreen", label=r"$D^{35}Cl$ $\nu=0$")
ax2.scatter(J_D_excited, D_excited, s = 10, color = "Navy", label=r"$D^{35}Cl$ $\nu=1$")

ax1.set_xlabel(r"$J^2 + J + 1$")

ax1.set_ylabel(r"(R(J-1) - P(J+1) / (J + 1/2), $\nu=0$")
ax2.set_ylabel(r"(R(J) - P(J) / (J + 1/2), $\nu=1$")

ax1.legend(loc = "best")

ax1.set_title("DCl FTIR spectrum")

plt.show()

m_H_ground = -0.0052
b_H_ground = 41.825

m_H_excited = -0.0041
b_H_excited = 40.552

m_D_ground = -0.0013
b_D_ground = 21.582

m_D_excited = -0.001
b_D_excited = 21.105

fig, ax1 = plt.subplots()
ax2 = ax1.twinx()

ax1.scatter([], [], color = "Navy", s = 10, label=r"$H^{35}Cl$ $\nu=1$")
ax1.scatter(J_H_ground, H_ground, s = 10, color = "Forestgreen", label=r"$H^{35}Cl$ $\nu=0$")
ax1.plot(J_H_ground, [(m_H_ground * i + b_H_ground) for i in J_H_ground], color = "Forestgreen")

ax2.scatter(J_H_excited, H_excited, s = 10, color = "Navy", label=r"$H^{35}Cl$ $\nu=1$")
ax2.plot(J_H_excited, [(m_H_excited * i + b_H_excited) for i in J_H_excited], color = "Navy")

ax1.set_xlabel(r"$J^2 + J + 1$")

ax1.set_ylabel(r"(R(J-1) - P(J+1) / (J + 1/2), $\nu=0$")
ax2.set_ylabel(r"(R(J) - P(J) / (J + 1/2), $\nu=1$")

ax1.legend(loc = "best")

ax1.set_title("HCl FTIR spectrum")

plt.show()

fig, ax1 = plt.subplots()
ax2 = ax1.twinx()

ax1.scatter([], [], color = "Navy", s = 10, label=r"$H^{35}Cl$ $\nu=1$")
ax1.scatter(J_D_ground, D_ground, s = 10, color = "Forestgreen", label=r"$H^{35}Cl$ $\nu=0$")
ax1.plot(J_D_ground, [(m_D_ground * i + b_D_ground) for i in J_D_ground], color = "Forestgreen")

ax2.scatter(J_D_excited, D_excited, s = 10, color = "Navy", label=r"$H^{35}Cl$ $\nu=1$")
ax2.plot(J_D_excited, [(m_D_excited * i + b_D_excited) for i in J_D_excited], color = "Navy")

ax1.set_xlabel(r"$J^2 + J + 1$")

ax1.set_ylabel(r"(R(J-1) - P(J+1) / (J + 1/2), $\nu=0$")
ax2.set_ylabel(r"(R(J) - P(J) / (J + 1/2), $\nu=1$")

ax1.legend(loc = "best")

ax1.set_title("DCl FTIR spectrum")

plt.show()
