def predictPartyVictory(senate):
    numR = 0
    numD = 0
    senate_list = list(senate)
    i = 0
    from collections import Counter
    people = Counter(senate_list)

    while people['R'] * people['D'] > 0:
        if senate_list[i] == 'R':
            if numD > 0:
                numD -= 1
                people['R'] -= 1
            else:
                senate_list.append('R')
                numR += 1

        else:
            if numR > 0:
                numR -= 1
                people['D'] -= 1
            else:
                numD += 1
                senate_list.append('D')
        i += 1
    if people['R'] > 0:
        return "Radiant"
    return 'Dire'


test = "RRDDDD"
print(predictPartyVictory(test))