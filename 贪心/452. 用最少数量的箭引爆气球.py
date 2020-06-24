def findMinArrowShots(points) -> int:
    points = sorted(points, key=lambda x: [x[0], x[1]])
    i = 1
    while i < len(points):
        if points[i][0] > points[i - 1][1]:
            i += 1
        else:
            start = max(points[i][0], points[i - 1][0])
            end = min(points[i][1], points[i - 1][1])
            points[i - 1] = [start, end]
            del points[i]

    return len(points)