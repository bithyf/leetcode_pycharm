def eraseOverlapIntervals(intervals):
    intervals = sorted(intervals, key=lambda x: [x[0], x[1]])
    erase = 0
    index = 1
    while index < len(intervals):
        if intervals[index][0] >= intervals[index - 1][1]:
            index += 1
        else:
            if intervals[index][0] == intervals[index - 1][0]:
                del intervals[index]

            elif intervals[index][0] < intervals[index - 1][1]:
                if intervals[index][1] < intervals[index - 1][1]:
                    del intervals[index - 1]
                else:
                    del intervals[index]
            erase += 1

    return erase

test = [[1, 2], [2, 3], [2, 4], [1, 3]]
print(eraseOverlapIntervals(test))
