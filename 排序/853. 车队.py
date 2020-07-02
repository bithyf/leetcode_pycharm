def carFleet(target, position, speed) -> int:
    p_s = [[position[i], speed[i]] for i in range(len(speed))]
    p_s.sort()
    time = [(target - element[0]) / element[1] for element in p_s]
    i = 1
    while i < len(time):
        if time[i] >= time[i - 1]:
            while 0 < i < len(time) and time[i] >= time[i - 1]:
                del time[i - 1]
                i -= 1
        i += 1
    return len(time)


target = 10
position = [0, 4, 2]
speed = [2,1,3]
print(carFleet(target,position,speed))



