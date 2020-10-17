def numIslands(self, grid):
    """
    :type grid: List[List[str]]
    :rtype: int
    """
    m = len(grid)
    if m == 0:
        return 0
    n = len(grid[0])
    num = 0

    def isone(i, j):
        if grid[i][j] == '1':
            grid[i][j] = '-1'
            if i + 1 < m:
                isone(i + 1, j)
            if j + 1 < n:
                isone(i, j + 1)
            if i > 0:
                isone(i - 1, j)
            if j > 0:
                isone(i, j - 1)

    for i in range(m):
        for j in range(n):
            if grid[i][j] == '1':
                num += 1
                isone(i, j)

    return num
