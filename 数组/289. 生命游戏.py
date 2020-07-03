def gameOfLife(board):
    """
        Do not return anything, modify board in-place instead.
        """
    for i in range(len(board)):
        for j in range(len(board[0])):
            board[i][j] = -board[i][j]
            up = max(0, i - 1)
            down = min(len(board) - 1, i + 1)
            left = max(0, j - 1)
            right = min(len(board[0]) - 1, j + 1)

            for m in range(up, down + 1):
                for n in range(left, right + 1):
                    board[i][j] += board[m][n] % 2 * 2

    for i in range(len(board)):
        for j in range(len(board[0])):
            m = board[i][j] // 2
            n = board[i][j] % 2
            if n == 0 and m == 3:
                board[i][j] = 1
            elif n == 1 and m < 2 or m > 3:
                board[i][j] = 0
            else:
                board[i][j] = n


test = [
    [0, 1, 0],
    [0, 0, 1],
    [1, 1, 1],
    [0, 0, 0]
]
gameOfLife(test)
print(test)
