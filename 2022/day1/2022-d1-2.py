with open('2022/day1/2022-d1-input.txt') as file:
    input = file.read().split('\n')

elfCalorieCount = 0
totalCount = 0
elvesCount = []

for value in input:
    if value != '':
        value = int(value)
        elfCalorieCount += value
    else:
        elvesCount.append(elfCalorieCount)
        totalCount += elfCalorieCount
        elfCalorieCount = 0

elvesCount.sort()
topThreeElves = elvesCount[-3:]
topThreeSum = sum(topThreeElves)
print('The three elves with the most calories carry {0} calories together.'.format(topThreeSum))