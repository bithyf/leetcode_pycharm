def dailyTemperatures(T):
    stack = []
    length = len(T)
    day = [0] * length

    for i in range(length):
        while len(stack) > 0 and T[stack[-1]] < T[i]:
            num = stack.pop()
            day[num] = i - num
        stack.append(i)

    while len(stack) > 0:
        num = stack.pop()
        day[num] = 0

    return day


test = [73, 74, 75, 71, 69, 72, 76, 73]
print(dailyTemperatures(test))
