paths = [['/']]
currentFolder = []
filesSize = {}
foldersSize = {}

def changeDirectory(cd: str) -> None:
    global currentFolder
    if cd == '/':
        currentFolder = ['/']
    elif cd == '..':
        currentFolder.pop(-1)
    else:
        currentFolder.append(cd)

def listedDirectory(dir: str) -> None:
    subFolder = list(currentFolder)
    subFolder.append(dir)
    global paths
    if subFolder not in paths:
        paths.append(subFolder)

def listedItem(size: int) -> None:
    if paths.index(currentFolder) in filesSize.keys():
        filesSize[paths.index(currentFolder)] += size
    else:
        filesSize[paths.index(currentFolder)] = size

def processEntry(cmd: str) -> None:
    if cmd[:4] == '$ cd':
        changeDirectory(cmd.split(' ')[-1])
    elif cmd[:4] == '$ ls': pass
    elif cmd[:4] == 'dir ':
        listedDirectory(cmd.split(' ')[-1])
    else:
        listedItem(int(cmd.split(' ')[0]))

def minimumFolderToFreeSpace(diskSize,neededSpace) -> int:
    foldersSizeVec = [filesSize[0]]
    maxIndex = max(list(foldersSize.keys()))
    for ind in range(1,maxIndex+1):
        foldersSizeVec.append(foldersSize[ind])

    currentFreeSpace = diskSize - foldersSizeVec[0]
    needToRemove = neededSpace - currentFreeSpace

    foldersSizeVec.sort()
    for value in foldersSizeVec:
        if needToRemove < value: return value

with open('2022/day7/2022-d7-input.txt') as file:
    entries = file.read().split('\n')
    entries.pop(-1)

for entry in entries:
    processEntry(entry)

revPaths = list(paths)
revPaths.reverse()
for path in revPaths[:-1]:
    if paths.index(path) in filesSize.keys():
        if paths.index(path) in foldersSize.keys(): foldersSize[paths.index(path)] += filesSize[paths.index(path)]
        else: foldersSize[paths.index(path)] = filesSize[paths.index(path)]
    else:
        if paths.index(path) not in foldersSize.keys(): foldersSize[paths.index(path)] = 0

    if paths.index(path[:-1]) in filesSize.keys(): filesSize[paths.index(path[:-1])] += foldersSize[paths.index(path)]
    else: filesSize[paths.index(path[:-1])] = foldersSize[paths.index(path)]
        

cumSum = 0
for folder in foldersSize:
    if foldersSize[folder] <= 100000:
        cumSum += foldersSize[folder]

minFolder = minimumFolderToFreeSpace(70000000,30000000)

print('The sum of the sizes of all the folders whose size is lower than 100000 bytes is {0}.'.format(cumSum))
print('The minimum folder size that can be removed to meet the needed space requirement is {0}'.format(minFolder))