import numpy as np

data = np.loadtxt("input.txt", dtype = str)
data = np.array([[int(d) for d in line] for line in data])

#print(data)
top_vis = np.zeros((len(data), len(data[0])), dtype=int)
bot_vis = np.zeros((len(data), len(data[0])), dtype=int)
left_vis = np.zeros((len(data), len(data[0])), dtype=int)
right_vis = np.zeros((len(data), len(data[0])), dtype=int)



def seen_from_top(data, row, col):
    if row == len(data):
        return 0
    tree = data[row, col]
    acc = 0
    for i in reversed(range(row)):
        #print(i)
        acc+=1
        if tree <= data[i, col]:
            break;
    return acc

def seen_from_left(data, row, col):
    if col == len(data[0]):
        return 0
    tree = data[row, col]
    acc = 0
    for i in reversed(range(col)):
        acc+=1
        #print(i)
        if tree <= data[row, i]:
            break;
    return acc

def seen_from_right(data, row, col):
    if col == 0:
        return 0
    tree = data[row, col]
    acc=0
    width = len(data[0])
    for i in range(width-col-1):
        #print(i+col+1)
        #print(data[row, width-i-1])
        acc+=1
        if tree <= data[row, i+col+1]:
            break;
    return acc

def seen_from_bot(data, row, col):
    if row == 0:
        return 0
    tree = data[row, col]
    acc = 0
    height = len(data)
    for i in range(height-row-1):
        #print(i)
        acc+=1
        if tree <= data[row+i+1, col]:
            break;
    return acc

def compute_score(data, row, col):
    return (seen_from_bot(data, row, col) * seen_from_right(data, row, col) * seen_from_left(data, row, col) * seen_from_top(data, row, col))

#vis_tree = len(data)*2+(len(data[0])-2)*2

best = 0

for i in range(len(data)):
    for j in range(len(data)):
        #print(data[i, j])
        score = compute_score(data, i, j)
        #print(score)
        #print()
        if score > best:
            best_cord = (i, j)
            best = score
#print()
print(best)
print(data[best_cord])
print(best_cord)

