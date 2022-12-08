import numpy as np

data = np.loadtxt("input.txt", dtype=str)

hand_trans = {
    'A': 1,#rock
    'B': 2,#paper
    'C': 3, #scissor
}

def decide_outcome(opp, me):
    if me == 'Y': #draw case
        return 3 + hand_trans[opp] #add my hand's points
    if me == 'X': #lose case. Return only your hand's points
        if opp == 'A':
            return hand_trans['C']
        elif opp == 'B':
            return hand_trans['A']
        elif opp == 'C':
            return hand_trans['B']
    if me == 'Z':
        if opp == 'A':
            return 6 + hand_trans['B']
        if opp == 'B':
            return 6 + hand_trans['C']
        if opp == 'C':
            return 6 + hand_trans['A']


#def char_to_hand(x):
#    if x=='A':
#        return "rock"
#    elif x=='B':
#        return "paper"
#    elif x == 'C':
#        return "scissors"
#    else:
#        print("error")


#def decide_outcome(opp, me):
#    me_hand = char_to_hand(me)
#    they_hand = char_to_hand(opp)
#    if me_hand==they_hand:
#        return 3 #tie
#    else:
#        if me_hand == "paper":
#            if they_hand == "rock":
#                return 6
#            else:
#                return 0
#        if me_hand == "scissors":
#            if they_hand == "paper":
#                return 6
#            else:
#                return 0
#        if me_hand == "rock":
#            if they_hand == "scissors":
#                return 6
#            else:
#                return 0

score = 0
l = len(data)
for i in range(l):
    s = decide_outcome(data[i, 0], data[i, 1])
    score += s
    #score += hand_trans[char_to_hand(data[i, 1])]


print(score)
