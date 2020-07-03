def uniquePathsWithObstacles(obstacleGrid):
    lenx = len(obstacleGrid)
    leny = len(obstacleGrid[0])
    path = [[] for i in range(lenx)]
    for i in range(lenx):
        path[i] = [0 for i in range(leny)]

    for i in range(len(obstacleGrid) - 1, -1, -1):
        for j in range(len(obstacleGrid[0]) - 1, -1, -1):
            if obstacleGrid[i][j] == 1:
                path[i][j] = 0
            elif i == len(obstacleGrid) - 1 and j == len(obstacleGrid[0]) - 1:
                path[i][j] = 1

            else:
                if i == len(obstacleGrid) - 1:
                    path[i][j] = path[i][j + 1]
                elif j == len(obstacleGrid[0]) - 1:
                    path[i][j] = path[i + 1][j]
                else:
                    path[i][j] = path[i][j + 1] + path[i + 1][j]

    return path[0][0]





    # def countpath(x, y, path, obstacleGrid):
    #     if x == len(obstacleGrid) or y == len(obstacleGrid[0]) or obstacleGrid[x][y] == 1:
    #         return 0
    #     elif x == len(obstacleGrid) - 1 and y == len(obstacleGrid[0]) - 1:
    #             # or (x == len(obstacleGrid) - 2 and y == len(obstacleGrid[0]) - 1):
    #         return 1
    #     else:
    #         return countpath(x + 1, y, path, obstacleGrid) + countpath(x, y + 1, path, obstacleGrid)
    # return countpath(0, 0, path, obstacleGrid)




obstacleGrid = [
  [0]
]
print(uniquePathsWithObstacles(obstacleGrid))