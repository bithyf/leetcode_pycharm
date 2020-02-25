def minimumTotal(triangle):
    length = len(triangle)
    if length == 1:
        return triangle[0][0]
    paths = [[triangle[0][0]]]
    for i in range(1, length):
        path = []
        for j in range(len(triangle[i])):
            if j - 1 < 0:
                path.append(triangle[i][j] + paths[i - 1][j])
            elif j == len(triangle[i]) - 1:
                path.append(triangle[i][j] + paths[i - 1][j - 1])
            else:
                path.append(triangle[i][j] + min(paths[i - 1][j], paths[i - 1][j - 1]))
        paths.append(path)
    return min(paths[length - 1])


triangle = [
    [2],
]
print(minimumTotal(triangle))
