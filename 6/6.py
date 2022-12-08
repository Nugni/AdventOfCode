import numpy as np

f = open("input.txt", 'r')

data = f.readlines()[0]
f.close()

length = len(data)
buffer = ["a" for x in range(14)]

def found_mark(buf):
    return not (len(set(buf)) < 14)

ccount = 0

for i in range(14):
    buffer[i] = data[i]
    ccount += 1

while True:
    if found_mark(buffer):
        print(ccount)
        break;
    if ccount == length:
        print("no marker")
        break
    for i in range(13):
        buffer[i] = buffer[i+1]
    buffer[13] = data[ccount]
    ccount += 1
