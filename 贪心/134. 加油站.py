def canCompleteCircuit(gas, cost):
    left = [gas[i] - cost[i] for i in range(len(gas))]
    if sum(left) < 0:
        return -1
    i = 0
    while i < len(gas):
        contain = left[i]
        width = 1
        while width < len(left) and contain >= 0:
            contain += left[(i + width) % len(left)]
            width += 1
        if width == len(left) and contain >= 0:
            return i
        i += width




gas = [5,1,2,3,4]
cost = [4,4,1,5,1]
print(canCompleteCircuit(gas,cost))