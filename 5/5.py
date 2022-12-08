import numpy as np
import re

f = open("input.txt", 'r')

line = f.readline()
llength = len(line)
#print(llength)
num_of_stacks = int((llength+1)/4)
#print(num_of_stacks)

box_idx = [i*4+1 for i in range(num_of_stacks)] #placement of possible boxes
#print(box_idx)
stacks = [[] for i in range(len(box_idx))]
#stacks[0].append(2)
#print(stacks)

while True:          #make stacks
    if not line:    #error handling
        break
    if line[0] == "\n":
        break;
    else:           #make stacks
        for i in range(num_of_stacks):
            if not line[box_idx[i]] == " ": #if there is a crate, add it
                elm = line[box_idx[i]]
                if elm.isnumeric():
                    break;
                else:
                    stacks[i].append(elm)

    line = f.readline()

for i in range(num_of_stacks):
    stacks[i].reverse()

#print(stacks)
line = f.readline()
instructions = []
#
while True:  #make movement
    if not line:    #error handling
        break
    else:
        instruct = line.split()
        instruct = [int(x) for x in instruct if x.isnumeric()]
        instructions.append(instruct)
    line = f.readline()
    #print(line)
    #print(1)
#print(instructions)

f.close()

print(stacks)
def move_crates(ins, sta):
    num = ins[0]
    fro = ins[1]-1
    to = ins[2]-1
    #for i in range(num):
    #    elm = sta[fro].pop()    #extend, remove
    #    sta[to].append(elm)
    lfro = len(sta[fro])
    elm = sta[fro][lfro-num:lfro]
    del sta[fro][lfro-num:lfro]
    sta[to].extend(elm)
    print(elm)
    #print(sta)

    return sta

for i in range(len(instructions)):
    stacks = move_crates(instructions[i], stacks)
    #print(stacks)

#print(stacks)
res = ""

for i in range(num_of_stacks):
    res = res +(stacks[i].pop())
print(res)