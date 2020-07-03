def minPathSum(grid):
    for i in range(1, len(grid)):
        grid[i][0] += grid[i - 1][0]
    for j in range(1, len(grid[0])):
        grid[0][j] += grid[0][j - 1]
    for i in range(1, len(grid)):
        for j in range(1, len(grid[0])):
            grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])
    return grid[len(grid) - 1][len(grid[0]) - 1]
grid = [
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
print(minPathSum(grid))