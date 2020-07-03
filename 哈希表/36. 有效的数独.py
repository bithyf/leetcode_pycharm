"""
判断一个 9x9 的数独是否有效。只需要根据以下规则，验证已经填入的数字是否有效即可。
"""


def isValidSudoku(board):
    row = [[0] * 10 for i in range(9)]
    col = [[0] * 10 for i in range(9)]
    box = [[0] * 10 for i in range(9)]
    for i in range(9):
        for j in range(9):
            if board[i][j] is '.':
                continue
            num = int(board[i][j])
            if row[i][num] == 1:
                return False
            if col[j][num] == 1:
                return False
            if box[i // 3 * 3 + j // 3][num] == 1:
                return False
            row[i][num] = 1
            col[num][j] = 1
            box[i // 3 * 3 + j // 3][num] = 1
    return True


test = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
print(isValidSudoku(test))