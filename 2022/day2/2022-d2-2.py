challenges = {'A':{'X':'C','Y':'A','Z':'B'},'B':{'X':'A','Y':'B','Z':'C'},'C':{'X':'B','Y':'C','Z':'A'}}

pointsFor = {'A':1,'B':2,'C':3,'X':0,'Y':3,'Z':6}

with open('2022/day2/2022-d2-input.txt') as file:
    strategyGuide = file.read().split('\n')
    strategyGuide.pop(-1)

totalPoints = []

for play in strategyGuide:
    roundPoints = 0

    vsPlay = play[0]
    result = play[2]

    myPlay = challenges.get(vsPlay).get(result)
    
    totalPoints.append(pointsFor.get(myPlay) + pointsFor.get(result))
    
print('Total points: {0}'.format(sum(totalPoints)))