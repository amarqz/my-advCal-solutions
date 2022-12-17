import numpy as np
import time

numberOfTails = 1

class Grid:
    def __init__(self,height:int,width:int,startPosition:list):
        self.height = height
        self.width = width
        self.startPosition = startPosition
        self._createGrid()

    def _createGrid(self):
        self.grid = np.zeros((self.height,self.width))
        self.visited = np.zeros((self.height,self.width))
        self.visited[self.startPosition[0]][self.startPosition[1]] = 1

    def countVisited(self) -> int:
        rowsSum = []
        for row in self.visited:
            rowsSum.append(sum(row))
        return sum(rowsSum)

    def printGrid(self):
        for i in range(0,self.height):
            row1 = ''
            row2 = ''
            for j in range(0,self.width):
                row1 += str(int(self.grid[i][j]))
                row2 += str(int(self.visited[i][j]))
            print('{0} {1}'.format(row1,row2))
        print('\n')
        time.sleep(2)

class Tail:
    def __init__(self,grid:Grid,id:int):
        self._grid = grid
        self._position = list(grid.startPosition)
        self._id = id
        if self._id < numberOfTails:
            self._tail = Tail(grid,self._id+1)
        else: self._tail = None
        self._headPosition = list(grid.startPosition)
        self._oldHeadPosition = []

    def _checkHAroundT(self) -> bool:
        if self._position == self._headPosition: return True
        if [self._position[0]-1,self._position[1]] == self._headPosition: return True
        if [self._position[0]+1,self._position[1]] == self._headPosition: return True
        if [self._position[0],self._position[1]-1] == self._headPosition: return True
        if [self._position[0],self._position[1]+1] == self._headPosition: return True
        if [self._position[0]-1,self._position[1]-1] == self._headPosition: return True
        if [self._position[0]+1,self._position[1]+1] == self._headPosition: return True
        if [self._position[0]-1,self._position[1]+1] == self._headPosition: return True
        if [self._position[0]+1,self._position[1]-1] == self._headPosition: return True
        return False

    def followUp(self,headPos:list):
        self._oldHeadPosition = list(self._headPosition)
        self._headPosition = list(headPos)

        if self._checkHAroundT(): pass
        else:
            self._grid.grid[self._position[0]][self._position[1]] = 0
            self._position = list(self._oldHeadPosition)
            self._grid.grid[self._position[0]][self._position[1]] = self._id
            if self._tail == None: self._grid.visited[self._position[0]][self._position[1]] = 1
            else: self._tail.followUp(self._position)
        

class Head:
    def __init__(self,grid:Grid):
        self._grid = grid
        self.position = list(grid.startPosition)
        self._tail = Tail(grid,1)

    def moveUp(self,times:int):
        for i in range(0,times):
            self._grid.grid[self.position[0]][self.position[1]] = 0
            self.position[0] -= 1
            self._grid.grid[self.position[0]][self.position[1]] = 1
            self._tail.followUp(self.position)
            #self._grid.printGrid()

    def moveDn(self,times:int):
        for i in range(0,times):
            self._grid.grid[self.position[0]][self.position[1]] = 0
            self.position[0] += 1
            self._grid.grid[self.position[0]][self.position[1]] = 1
            self._tail.followUp(self.position)
            #self._grid.printGrid()

    def moveLt(self,times:int):
        for i in range(0,times):
            self._grid.grid[self.position[0]][self.position[1]] = 0
            self.position[1] -= 1
            self._grid.grid[self.position[0]][self.position[1]] = 1
            self._tail.followUp(self.position)
            #self._grid.printGrid()

    def moveRt(self,times:int):
        for i in range(0,times):
            self._grid.grid[self.position[0]][self.position[1]] = 0
            self.position[1] += 1
            self._grid.grid[self.position[0]][self.position[1]] = 1
            self._tail.followUp(self.position)
            #self._grid.printGrid()

with open('2022/day9/2022-d9-input.txt') as file:
    commands = file.read().split('\n')
    commands.pop(-1)

newGrid = Grid(500,500,[30,30])
head = Head(newGrid)

for command in commands:
    command = command.split(' ')
    direction = command[0]
    repetitions = int(command[1])

    match direction:
        case 'U': head.moveUp(repetitions)
        case 'D': head.moveDn(repetitions)
        case 'L': head.moveLt(repetitions)
        case 'R': head.moveRt(repetitions)

print('The tail visited {0} positions.'.format(newGrid.countVisited()))