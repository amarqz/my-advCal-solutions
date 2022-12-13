def findSeparation(data):
    index = 0
    for entry in data:
        if entry == '':
            return index
        index += 1

def processPiles(data):
    data.reverse()
    piles = [[],[],[],[],[],[],[],[],[]]

    for entry in data:
        for count in range(0,9):
            if entry[1+count*4] != ' ':
                piles[count].append(entry[1+count*4])        
    return piles

def moveAction(piles,actions):
    crane = []
    for statement in actions:
        statement = statement.split(' ')
        howMany = int(statement[1])
        whereFrom = int(statement[3])-1
        whereTo = int(statement[5])-1

        for i in range(1,howMany+1):
            crane.append(piles[whereFrom].pop())
        
        for i in range(1,howMany+1):
            piles[whereTo].append(crane.pop())
    return piles


with open('2022/day5/2022-d5-input.txt') as file:
    rawData = file.read().split('\n')
    rawData.pop(-1)

sepIndex = findSeparation(rawData)
oldPiles = processPiles(rawData[:sepIndex-1])
newPiles = moveAction(oldPiles,rawData[sepIndex+1:])

sumBoxes = 0
for pile in newPiles:
    print(pile[-1])