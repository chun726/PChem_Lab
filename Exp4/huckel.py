print("="*30)
print("Huckel method calculator")
print("="*30)

import numpy as np

# Values and inputs
approximation = 0.001
step = 0.00001
accuracy = 0.0001
count = 0
x_value = [0]
y_value = []
cyclic = int(input("Choose if your molecule is cyclic(0 = linear, 1 = cyclic): "))
carbon = int(input("Enter the number of carbon in your molecule: "))
hydrogen = carbon

if cyclic == 0:
    hydrogen += 2


huckel = np.zeros((carbon, carbon))

# Matrix initialization
for i in range(carbon):
    huckel[i][i] = approximation
    if i == 0:
        huckel[i][i + 1] = 1
    elif i == carbon - 1:
        huckel[i][i - 1] = 1
    else:
        huckel[i][i + 1] = 1
        huckel[i][i - 1] = 1
        
if (cyclic == 1):
    huckel[0][carbon - 1] = 1
    huckel[carbon - 1][0] = 1

# Iteration
for i in range(int(1e6)):
    if (abs(np.linalg.det(huckel)) < accuracy):
        if abs(x_value[-1] - huckel[0][0]) >= 0.05:
            x_value.append(huckel[0][0])
            y_value.append(-huckel[0][0])
        
    for j in range(carbon):
        huckel[j][j] += step
    
    if (i > 1e5 and i%1e5 == 0):
        print("processing" + "."*(i//int(1e5)))

x_value.pop(0)
beta_value = x_value + y_value

# Information
print("\n")
print("="*20)
print("Result section")
print("="*20)

print("Molecular formula of your molecule is", end = " ")
print(f"C{carbon}H{hydrogen}")

print("From α + c * β, c values are", end = " ")
for i in beta_value:
    print(round(i, 4), end = " ")
print("\n")

print("Energy level of HOMO is", end = " ")
print(f"α + {round(min(x_value), 3)} * β")
print("Energy level of LUMO is", end = " ")
print(f"α + {round(-min(x_value), 3)} * β")

print("\n*Degenerated values are omitted")



