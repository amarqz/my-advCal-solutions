def checkIfMarkerOrMessage(lastF):
    if len(set(lastF)) == len(lastF): return True
    else: return False

def findFirstMarker(signal):
    lastFour = []
    count = 0

    for char in signal:
        if len(lastFour) == 4:
            if checkIfMarkerOrMessage(lastFour): return count
            lastFour.pop(0)
        lastFour.append(char)
        count += 1

def findFirstMessage(signal):
    lastFourteen = []
    count = 0

    for char in signal:
        if len(lastFourteen) == 14:
            if checkIfMarkerOrMessage(lastFourteen): return count
            lastFourteen.pop(0)
        lastFourteen.append(char)
        count += 1

with open('2022-d6-input.txt') as file:
    signal = file.read().split('\n')
    signal = signal[:-1][0]

firstMarkerIndex = findFirstMarker(signal)
firstMsgIndex = findFirstMessage(signal)

print('The first marker is found at index: {0}'.format(firstMarkerIndex))
print('The first message is found at index: {0}'.format(firstMsgIndex))