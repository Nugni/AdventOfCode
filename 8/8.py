import numpy as np

data = np.loadtxt("input.txt", dtype = str)
data = np.array([[int(d) for d in line] for line in data])

#print(data)
top_vis = np.zeros((len(data), len(data[0])), dtype=int)
bot_vis = np.zeros((len(data), len(data[0])), dtype=int)
left_vis = np.zeros((len(data), len(data[0])), dtype=int)
right_vis = np.zeros((len(data), len(data[0])), dtype=int)



def seen_from_top(data, row, col):
    tree = data[row, col]
    for i in range(row):
        #print(data[i, col])
        if tree <= data[i, col]:
            return False
    return True

def seen_from_left(data, row, col):
    tree = data[row, col]
    for i in range(col):
        if tree <= data[row, i]:
            return False
    return True

def seen_from_right(data, row, col):
    tree = data[row, col]
    width = len(data[0])
    for i in range(width-col-1):
        if tree <= data[row, width-i-1]:
            return False
    return True

def seen_from_bot(data, row, col):
    tree = data[row, col]
    height = len(data)
    for i in range(height-row-1):
        if tree <= data[height-i-1, col]:
            return False
    return True

def is_seen(data, row, col):
    return seen_from_bot(data, row, col) or seen_from_right(data, row, col) or seen_from_left(data, row, col) or seen_from_top(data, row, col)

vis_tree = len(data)*2+(len(data[0])-2)*2

for i in range(len(data)-2):
    for j in range(len(data)-2):
        if is_seen(data, i+1, j+1):
            #print(data[i+1, j+1])
            vis_tree += 1
print(vis_tree)

