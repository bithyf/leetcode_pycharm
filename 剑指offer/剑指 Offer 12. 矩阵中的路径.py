def exist(board, word) -> bool:
    def match(b, index_i, index_j, index):
        if b[index_i][index_j] and b[index_i][index_j] == word[index]:
            if index + 1 == len(word):
                return True
            t = b[index_i][index_j]
            b[index_i][index_j] = None
            if index_i - 1 >= 0:
                if match(b, index_i - 1, index_j, index + 1):
                    return True

            if index_i + 1 < len(b):
                if match(b, index_i + 1, index_j, index + 1):
                    return True

            if index_j + 1 < len(b[0]):
                if match(b, index_i, index_j + 1, index + 1):
                    return True

            if index_j - 1 >= 0:
                if match(b, index_i, index_j - 1, index + 1):
                    return True
            b[index_i][index_j] = t
        return False

    for i in range(len(board)):
        for j in range(len(board[0])):
            if match(board, i, j, 0) is True:
                return True
    return False


matrix = [["C", "A", "A"], ["A", "A", "A"], ["B", "C", "D"]]
target = "AAB"

if exist(matrix, target):
    print('y')
else:
    print('f')
