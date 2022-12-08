import numpy as np

data = np.loadtxt("input.txt", dtype = str, delimiter=",")

def check_overlap(pair):
    int1 = [int(x) for x in pair[0].split("-")]
    int2 = [int(x) for x in pair[1].split("-")]
    #if int1[0] >= int2[0] and
    #    return 1
    #elif int1[0] <= int2[0] and int1[1] >= int2[1]:
    #    return 1
    #else:
    #    return 0
    if int1[0] < int2[0]:
        if int1[1] >= int2[0]:
            return 1
        else:
            return 0
    elif int2[0] < int1[0]:
        if int2[1] >= int1[0]:
            return 1
        else:
            return 0
    else:
        return 1
#print(data)

acc = 0
length = len(data)
for i in range(length):
    c = check_overlap(data[i])
    #if c == 1:
    #    print(data[i])
    acc += c

print(acc)

#d = [int(x) for x in data[0, 0].split("-")]
#print(d)
#print(data[0, 0].split("-"))