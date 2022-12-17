import numpy as np

module = []

class Monkey:
    def __init__(self,id:int,data):
        self.id = int(id)
        self._itemsData = data[0]
        self.items = []
        self._operation = str(data[1].split('  ')[1].split(' ')[4])
        self._operand = int(data[1].split('  ')[1].split(' ')[5]) if not data[1].split('  ')[1].split(' ')[5] == 'old' else 'old'
        self._divider = int(data[2].split('  ')[1].split(' ')[3])
        module.append(self._divider)
        self._trueReceptor = int(data[3].split('    ')[1].split(' ')[5])
        self._falseReceptor = int(data[4].split('    ')[1].split(' ')[5])
        self.inspectedItems = 0

    def modularItems(self):
        self.items = [[int(x)%y for y in module] for x in [x.replace(',','') for x in self._itemsData.split('  ')[1].split(' ')][2:]]

    def inspectItem(self):
        item = self.items.pop(0)
        worryLevel = list(item)
        if self._operand != 'old':
            if self._operation == '+': worryLevel = list(map(lambda x: x + self._operand,item))
            elif self._operation == '*': worryLevel = list(map(lambda x: x * self._operand,item))
        else:
            if self._operation == '+': worryLevel = list(map(lambda x: x * 2,item))
            elif self._operation == '*': worryLevel = list(map(lambda x: x ** 2,item))

        self.inspectedItems += 1

        if worryLevel[self.id] % self._divider == 0: monkeys[self._trueReceptor]._send(list(map(lambda x,y: x%y, worryLevel, module)))
        else: monkeys[self._falseReceptor]._send(list(map(lambda x,y: x%y, worryLevel, module)))

    def _send(self,item:int):
        self.items.append(item)

with open('2022/day11/input.txt') as file:
    monkeyData = file.read()[:-1].split('\n\n')

monkeys = []
for monkey in monkeyData:
    id = monkey.split('\n')[0].split(' ')[1][:-1]
    data = monkey.split('\n')[1:]
    monkeys.append(Monkey(id,data))

for monkey in monkeys:
    monkey.modularItems()

for round in range(0,10000):
    for monkey in monkeys:
        for item in range(0,len(monkey.items)):
            monkey.inspectItem()
    print('Round {0} completed.'.format(round+1))

inspectedItemsPerMonkey = []
for monkey in monkeys:
    inspectedItemsPerMonkey.append(monkey.inspectedItems)
inspectedItemsPerMonkey.sort()
monkeyBusiness = np.prod(inspectedItemsPerMonkey[-2:],dtype=object)

print("The two most active monkeys' business is {0}".format(monkeyBusiness))