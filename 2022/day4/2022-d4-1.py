def doesFullyContain(pair):
    pairOne = pair[0].split('-')
    pairTwo = pair[1].split('-')

    if (int(pairOne[0]) >= int(pairTwo[0]) and int(pairOne[1]) <= int(pairTwo[1])) or (int(pairTwo[0]) >= int(pairOne[0]) and int(pairTwo[1]) <= int(pairOne[1])):
        return 1
    else:
        return 0

def doesPartiallyContain(pair):
    pairOne = pair[0].split('-')
    pairTwo = pair[1].split('-')

    for i in range(int(pairOne[0]),int(pairOne[1])+1):
        for j in range(int(pairTwo[0]),int(pairTwo[1])+1):
            if i == j:
                return 1
    return 0

with open('2022/day4/2022-d4-input.txt') as file:
    assignments = file.read().split('\n')
    assignments.pop(-1)

countF = 0
countP = 0

for assignment in assignments:
    pair = assignment.split(',')
    countF += doesFullyContain(pair)
    countP += doesPartiallyContain(pair)

print('The sum of fully overlapping tasks is {0}, whereas the sum of partially overlapping tasks is {1}.'.format(countF,countP))