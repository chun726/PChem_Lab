data = [0.31742041185215053, 0.3245110915135041, 0.29148467775775083, 
        0.31806333496276157, 0.28579002910724427, 0.28017985669086104, 
        0.3010299956639812, 0.2808266095756942]
grubbs = []
critical_value = 2.126

def mean(sample):
    return sum(sample)/len(sample)

def standard_dev(sample, avg):
    count = 0
    for i in sample:
        count += (i - avg)**2
    count /= (len(sample) - 1)
    return count**0.5

def G_test(sample, avg, sd):
    global grubbs
    for i in sample:
        temp = abs(i - avg)/sd
        grubbs.append(temp)

data_avg = mean(data)
data_s = standard_dev(data, data_avg)
G_test(data, data_avg, data_s)

for i in grubbs:
    if i >= critical_value:
        print(True)
    else:
        print(False)

