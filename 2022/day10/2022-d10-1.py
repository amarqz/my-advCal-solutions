cycle = 1
probedCycles = [20, 60, 100, 140, 180, 220]
registerValue = 1
signalStrSum = 0

with open('2022/day10/input.txt') as file:
    commands = file.read().split('\n')
    commands.pop(-1)

for command in commands:
    if command == 'noop':
        if cycle in probedCycles: signalStrSum += cycle*registerValue
    else:
        if cycle in probedCycles: signalStrSum += cycle*registerValue
        cycle += 1
        if cycle in probedCycles: signalStrSum += cycle*registerValue
        registerValue += int(command.split(' ')[1])
    cycle += 1

print('The sum of the probed signal strengths is {0}.'.format(signalStrSum))