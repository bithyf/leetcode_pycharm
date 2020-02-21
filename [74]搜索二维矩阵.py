def searchMatrix(matrix, target):
    row = len(matrix)
    col = len(matrix[0])

    b = row * col - 1
    f = 0
    while b >= f:
        mid = (b + f) // 2
        i = mid // col
        j = mid % col
        if target == matrix[i][j]:
            return True

        elif target > matrix[i][j]:
            f = mid + 1
        else:
            b = mid - 1
    return False


matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 13
searchMatrix(matrix, target)
