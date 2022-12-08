import numpy as np

def to_int(x):
    if ord(x) > 96:
        return ord(x)-96
    else:
        return ord(x) - 38

#print(ord('A'))

data = np.loadtxt("input.txt", dtype=str)
length = int(len(data)/3)
overlap = np.zeros(length)


for i in range(length):
    row1 = data[3*i]
    row2 = data[3*i+1]
    row3 = data[3*i+2]

    #r_length = len(row)
    #mid = int(r_length/2)
    #elm = list(set(row[0:mid]) & set(row[mid:]))[0]
    elm = list(set(row1) & set(row2) & set(row3))[0]
    #print(elm)
    overlap[i] = to_int(elm)

print(int(sum(overlap)))