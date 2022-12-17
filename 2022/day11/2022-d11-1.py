import numpy as np

class Monkey:
    def __init__(self,id:int,data):
        self.id = id
        self.items = [int(x) for x in [x.replace(',','') for x in data[0].split('  ')[1].split(' ')][2:]]
        self._operation = str(data[1].split('  ')[1].split(' ')[4])
        self._operand = int(data[1].split('  ')[1].split(' ')[5]) if not data[1].split('  ')[1].split(' ')[5] == 'old' else 'old'
        self._divider = int(data[2].split('  ')[1].split(' ')[3])
        self._trueReceptor = int(data[3].split('    ')[1].split(' ')[5])
        self._falseReceptor = int(data[4].split('    ')[1].split(' ')[5])
        self.inspectedItems = 0

    def inspectItem(self):
        item = self.items.pop(0)
        if self._operand != 'old':
            if self._operation == '+': worryLevel = item + self._operand
            elif self._operation == '*': worryLevel = item * self._operand
        else:
            if self._operation == '+': worryLevel = 2 * item
            elif self._operation == '*': worryLevel = item ** 2
        worryLevel = int(worryLevel/3)

        self.inspectedItems += 1

        if worryLevel % self._divider == 0: monkeys[self._trueReceptor]._send(worryLevel)
        else: monkeys[self._falseReceptor]._send(worryLevel)

    def _send(self,item:int):
        self.items.append(item)

with open('2022/day11/input.txt') as file:
    monkeyData = file.read()[:-1].split('\n\n')

monkeys = []
for monkey in monkeyData:
    id = monkey.split('\n')[0].split(' ')[1][:-1]
    data = monkey.split('\n')[1:]
    monkeys.append(Monkey(id,data))

for round in range(0,20):
    for monkey in monkeys:
        for item in range(0,len(monkey.items)):
            monkey.inspectItem()

inspectedItemsPerMonkey = []
for monkey in monkeys:
    inspectedItemsPerMonkey.append(monkey.inspectedItems)
inspectedItemsPerMonkey.sort()
monkeyBusiness = np.prod(inspectedItemsPerMonkey[-2:])

print("The two most active monkeys' business is {0}".format(monkeyBusiness))