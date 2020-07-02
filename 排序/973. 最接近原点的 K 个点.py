def kClosest(points, K):
    def ojld(point):
        return point[0] ** 2 + point[1] ** 2
    f = 0
    b = len(points) - 1
    while True:
        midnum = points[f]
        while f < b:
            while f < b and ojld(points[b]) >= ojld(midnum):
                b -= 1
            points[f] = points[b]
            while f < b and ojld(points[f]) <= ojld(midnum):
                f += 1
            points[b] = points[f]
        points[f] = midnum
        if f == K - 1:
            return points[0:K]
        elif f > K - 1:
            f = 0
            b = b - 1
        else:
            f = f + 1
            b = len(points) - 1


points = [[0, 1], [1, 0]]
K = 2
print(kClosest(points, K))
