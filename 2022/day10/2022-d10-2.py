import numpy as np

registerValue = 1

class CRT:
    def __init__(self,height:int,width:int):
        self.grid = np.ones((height,width))
        self._height = height
        self._width = width
        self._cycle = [0,0]

    def drawOrNot(self,spriteCenter:int):
        draw = False
        if self._cycle == [self._cycle[0],spriteCenter] or \
            self._cycle == [self._cycle[0],spriteCenter-1] or \
                self._cycle == [self._cycle[0],spriteCenter+1]: draw = True
        if draw: self.grid[self._cycle[0]][self._cycle[1]] = 0

    def updateCycle(self):
        if self._cycle[1] < self._width-1: self._cycle[1] += 1
        else:
            self._cycle[0] += 1
            self._cycle[1] = 0

    def print(self):
        for row in self.grid:
            newRow = ''
            for column in row:
                char = '.' if int(column) == 1 else '#'
                newRow += char
            print(newRow)

with open('2022/day10/input.txt') as file:
    commands = file.read().split('\n')
    commands.pop(-1)

newCRT = CRT(6,40)
for command in commands:
    if command == 'noop':
        newCRT.drawOrNot(registerValue)
    else:
        newCRT.drawOrNot(registerValue)
        newCRT.updateCycle()
        newCRT.drawOrNot(registerValue)
        registerValue += int(command.split(' ')[1])
    newCRT.updateCycle()


newCRT.print()