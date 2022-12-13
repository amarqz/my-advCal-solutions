def priority(item: str):
    if item == item.lower():
        return ord(item)-96
    else:
        return ord(item)-38

def findRepeatedItem(bagOne,bagTwo,bagThree):

    for itemFirstBag in bagOne:
        for itemSecondBag in bagTwo:
            if itemFirstBag == itemSecondBag:
                for itemThirdBag in bagThree:
                    if itemFirstBag == itemThirdBag:
                        return priority(itemFirstBag)

with open('2022/day3/2022-d3-input.txt') as file:
    bags = file.read().split('\n')
    bags.pop(-1)

prioritySum = 0
for i in range(int(len(bags)/3)):
    prioritySum += findRepeatedItem(bags[3*i],bags[3*i+1],bags[3*i+2])

print('The sum of the priorities of the items found in both compartments of each bags is {0}.'.format(prioritySum))