import numpy as np

class Node:
    def __init__(self, name, is_dir, parent = None):
        self.name = name
        self.is_dir = is_dir
        self.parent = parent
        if self.parent is not None:
            self.parent.add_child(self)
        self.children = []
        self.size = 0

    def add_child(self, child):
        self.children.append(child)

    def add_size(self, size = 0):
        self.size += size
        if self.parent is not None:
            self.parent.add_size(size)

current_dir = None

f = open("input.txt", "r")
lines = f.readlines()

for line in lines:
    instr = line.split()
    #print(instr)
    #print(instr)
    if instr[0] == "$":
        if instr[1] == "cd":
            if instr[2] == "/":
                root = Node("/", True)
                current_dir = root
            elif instr[2] == "..":
                current_dir = current_dir.parent
            else:
                #print("current dir: {0}".format(instr[2]))
                #new_dir = Node(instr[2], True, current_dir)
                #current_dir = new_dir
                cur_name = instr[2]
                #print([child.name for child in current_dir.children if child.name == cur_name])
                current_dir = [child for child in current_dir.children if child.name == cur_name][0] #child where name = instr[2]
        #print("cur dir {0}".format(current_dir.name))
        #[print("its children {0}".format(x.name)) for x in current_dir.children]
        #print()
    else:
        obj_name = instr[1]
        dir_or_size = instr[0]
        #print(instr[0])
        if dir_or_size == "dir":
            #print("new dir: {0}".format(obj_name))
            new_dir = Node(obj_name, True, current_dir)
        else:
            #print("new file: {0}".format(obj_name))
            new_file = Node(obj_name, False, current_dir)
            new_file.add_size(int(dir_or_size))


smol_dir = []

max_space = 40000000
used_space = root.size
print(used_space)
space_needed = used_space-max_space
print(space_needed)

def treewalk(current_node):
    if len(current_node.children) < 1:
        return
    #print(current_node.size)
    if current_node.size >= space_needed and current_node.is_dir:
        smol_dir.append(current_node)
    [treewalk(child) for child in current_node.children]

treewalk(root)

smol_dir.sort(key=lambda x: x.size)

#print(len(smol_dir))

#[print(n.name) for n in smol_dir]
print([n.size for n in smol_dir][0])