def exist(board, word):
    row = len(board)
    if row == 0:
        return False
    col = len(board[0])
    if col == 0:
        return False

    def backtracking(i, j, k, tracking):
        if k == len(word):
            return True
        else:
            if tracking[i + 1][j + 1] == 1 or board[i][j] != word[k]:
                return False
            else:
                tracking[i + 1][j + 1] = 1
                if backtracking(i + 1, j, k + 1, list(tracking)) or \
                        backtracking(i - 1, j, k + 1, list(tracking)) or \
                        backtracking(i, j + 1, k + 1, list(tracking)) or \
                        backtracking(i, j - 1, k + 1, list(tracking)):
                    return True
                else:
                    tracking[i + 1][j + 1] = 0
                    return False

    mark = [[] for i in range(row + 2)]
    for i in range(len(mark)):
        mark[i] = [0 for j in range(col + 2)]
    for j in range(col + 2):
        mark[0][j] = 1
        mark[row + 1][j] = 1
    for j in range(1, row + 1):
        mark[j][0] = 1
        mark[j][col + 1] = 1
    for i in range(row):
        for j in range(col):
            if backtracking(i, j, 0, list(mark)):
                return True
    return False


board = [["C", "A", "A"], ["A", "A", "A"], ["B", "C", "D"]]
word = "bAB"
if exist(board, word):
    print('y')
else:
    print('n')

# row = 4
# col = 5
# mark = [[] for i in range(row + 1)]
# for i in range(len(mark)):
#     mark[i] = [0 for j in range(col + 1)]
# for j in range(col + 1):
#     mark[0][j] = 1
#     mark[row][j] = 1
# for j in range(1, row):
#     mark[j][0] = 1
#     mark[j][col] = 1
# print(mark)
