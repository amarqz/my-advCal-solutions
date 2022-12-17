def checkRow(row: int,column: int) -> int:
    treeHeight = int(grid[row][column])
    leftVisibility = 0
    rightVisibility = 0
    for newTree in range(column-1,-1,-1):
        if treeHeight <= int(grid[row][newTree]):
            leftVisibility += 1
            break
        else: leftVisibility += 1
    for newTree in range(column+1,width):
        if treeHeight <= int(grid[row][newTree]):
            rightVisibility += 1
            break
        else: rightVisibility += 1
    return leftVisibility * rightVisibility

def checkColumn(row: int,column: int) -> int:
    treeHeight = int(grid[row][column])
    upVisibility = 0
    downVisibility = 0
    for newTree in range(row-1,-1,-1):
        if treeHeight <= int(grid[newTree][column]):
            upVisibility += 1
            break
        else: upVisibility += 1
    for newTree in range(row+1,height):
        if treeHeight <= int(grid[newTree][column]):
            downVisibility += 1
            break
        else: downVisibility += 1
    return upVisibility * downVisibility

with open('2022/day8/2022-d8-input.txt') as file:
    grid = file.read().split('\n')
    grid.pop(-1)

height = len(grid)
width = len(grid[0])

scenicScores = []
for heightIndex in range(0,height):
    for widthIndex in range(0,width):
        rowScore = checkRow(heightIndex,widthIndex)
        colScore = checkColumn(heightIndex,widthIndex)
        scenicScores.append(rowScore * colScore)

print('The highest possible scenic score is {0}.'.format(max(scenicScores)))