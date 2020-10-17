def solve(self, board):
    """
    :type board: List[List[str]]
    :rtype: None Do not return anything, modify board in-place instead.
    """
    if not board:
        return
    length = len(board)
    width = len(board[0])

    def bfs(x, y):
        if x < 0 or y < 0 or x >= length or y >= width or board[x][y] != 'O':
            return
        board[x][y] = 'A'
        bfs(x - 1, y)
        bfs(x + 1, y)
        bfs(x, y - 1)
        bfs((x, y + 1))

    for i in range(length):
        bfs(i, 0)
        bfs(i, width - 1)
    for j in range(1, width - 1):
        bfs(0, j)
        bfs(length - 1, j)

    for i in range(length):
        for j in range(width):
            if board[i][j] == "O":
                board[i][j] = 'X'
            elif board[i][j] == "A":
                board[i][j] = 'O'


# def cstr(a):
#     a = 7
#
#
# a = [['a', 'b']]
# print(a[0][1] is "b")
a = -6
b = -6
print(a is b)
