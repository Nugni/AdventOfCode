import numpy as np
import pandas as pd

data = [[]]
i = 0
f = open("input.txt", "r")
for word in f:
    if word == "\n":
        i+=1
        data.append([])
    else:
        data[i].append(int(word))

sorte = sorted([sum(row) for row in data], reverse=True)

print(sum(sorte[0:3]))