def checkRow(row: int,column: int) -> bool:
    treeHeight = int(grid[row][column])
    leftVisibility = True
    rightVisibility = True
    for newTree in range(0,column):
        if treeHeight <= int(grid[row][newTree]):
            leftVisibility = False
            break
    for newTree in range(column+1,width):
        if treeHeight <= int(grid[row][newTree]):
            rightVisibility = False
            break
    if leftVisibility or rightVisibility: return True
    else: return False

def checkColumn(row: int,column: int) -> bool:
    treeHeight = int(grid[row][column])
    upVisibility = True
    downVisibility = True
    for newTree in range(0,row):
        if treeHeight <= int(grid[newTree][column]):
            upVisibility = False
            break
    for newTree in range(row+1,height):
        if treeHeight <= int(grid[newTree][column]):
            downVisibility = False
            break
    if upVisibility or downVisibility: return True
    else: return False

with open('2022/day8/2022-d8-input.txt') as file:
    grid = file.read().split('\n')
    grid.pop(-1)

height = len(grid)
width = len(grid[0])

visibleTrees = 2 * (height + width - 2)

for heightIndex in range(1,height-1):
    for widthIndex in range(1,width-1):
        if (checkRow(heightIndex,widthIndex) or checkColumn(heightIndex,widthIndex)):
            visibleTrees += 1

print('The number of visible trees from the outside is {0}.'.format(visibleTrees))