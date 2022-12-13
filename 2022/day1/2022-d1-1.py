with open('2022-d1-input.txt') as file:
    input = file.read().split('\n')

elfCalorieCount = 0
totalCount = 0
elfMaxCount = 0

for value in input:
    if value != '':
        value = int(value)
        elfCalorieCount += value
    else:
        elfMaxCount = max(elfMaxCount,elfCalorieCount)
        totalCount += elfCalorieCount
        elfCalorieCount = 0

print('The elf with the most calories has {0} calories.'.format(elfMaxCount))
print('All the elves carry a total of {0} calories.'.format(totalCount))