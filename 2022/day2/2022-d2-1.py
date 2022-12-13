shapes = {'A':'rock','B':'paper','C':'scissors','X':'rock','Y':'paper','Z':'scissors'}
challenges = [('rock','scissors'),('paper','rock'),('scissors','paper'),('scissors','rock'),('rock','paper'),('paper','scissors')]

def pointsForShape(inp):
    if inp == 'X':
        return 1
    elif inp == 'Y':
        return 2
    elif inp == 'Z':
        return 3

def challenge(my,vs):
    if shapes.get(my) == shapes.get(vs):
        return 3

    else:
        ind = challenges.index((shapes.get(my),shapes.get(vs)))
        res = 6 if ind <= 2 else 0
        return res


with open('2022-d2-input.txt') as file:
    strategyGuide = file.read().split('\n')
    strategyGuide.pop(-1)

totalPoints = []

for play in strategyGuide:
    roundPoints = 0

    vsPlay = play[0]
    myPlay = play[2]

    roundPoints += pointsForShape(myPlay)
    roundPoints += challenge(myPlay,vsPlay)

    totalPoints.append(roundPoints)
    
print('Total points: {0}'.format(sum(totalPoints)))