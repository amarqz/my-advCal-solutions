def priority(item: str):
    if item == item.lower():
        return ord(item)-96
    else:
        return ord(item)-38

def findRepeatedItem(bag):
    length = len(bag)

    for itemFirstCompartment in bag[:int(length/2)]:
        for itemSecondCompartment in bag[int(length/2):]:
            if itemFirstCompartment == itemSecondCompartment:
                return priority(itemFirstCompartment)
    return 0

with open('2022/day3/2022-d3-input.txt') as file:
    bags = file.read().split('\n')

prioritySum = 0
for bag in bags:
    prioritySum += findRepeatedItem(bag)

print('The sum of the priorities of the items found in both compartments of each bags is {0}.'.format(prioritySum))