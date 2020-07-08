def movingCount(m: int, n: int, k: int) -> int:
    visited = [[0] * n for i in range(m)]

    def visite(i, j):
        # print(visited)
        if i >= m or j >= n:
            return 0
        if visited[i][j] == 1:
            return 0
        visited[i][j] = 1
        if i % 10 + i // 10 + j % 10 + j // 10 <= k:
            return 1 + visite(i + 1, j) + visite(i, j + 1)
        return 0

    return visite(0, 0)


m = 2
n = 3
k = 1
print(movingCount(m, n, k))
