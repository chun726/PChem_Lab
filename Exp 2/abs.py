import csv
import matplotlib.pyplot as plt
from itertools import islice

x1 = []
y1 = []
x2 = []
y2 = []

with open(r"E:\test\THF_abs.csv", "r") as file:
    reader = csv.reader(file)
    row = list(reader)

skipped_rows_1 = islice(row, 2, len(row) - 33)

for row in skipped_rows_1:
    x1.append(float(row[0]))
    y1.append(float(row[1]))

with open(r"E:\test\cyclo_abs.csv", "r") as file:
    reader = csv.reader(file)
    row = list(reader)
    
skipped_rows_2 = islice(row, 2, len(row) - 33)

for row in skipped_rows_2:
    x2.append(float(row[0]))
    y2.append(float(row[1]))
    
x1 = x1[::-1]
x2 = x2[::-1]
y1 = y1[::-1]
y2 = y2[::-1]

#=============================================#

print("1 - THF, 2 - Cyclohexane")
print("Choose: ", end = "")
op = int(input())

plt.figure(dpi = 1200)
plt.xlabel("Wavelength (nm)")
plt.ylabel("Abs")

if op == 1:
    plt.plot(x1, y1, color = "forestgreen", label = "THF")
    
elif op == 2:
    plt.plot(x2, y2, color = "royalblue", label = "Cyclohexane")

plt.legend(loc = "best")
plt.show()



























