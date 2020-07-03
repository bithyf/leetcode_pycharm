def findNumberIn2DArray(matrix, target) -> bool:
    if len(matrix) == 0:
        return False
    i = 0
    j = len(matrix[0]) - 1

    while i < len(matrix) and j >= 0 and matrix[i][j] != target:
        if matrix[i][j] > target:
            j -= 1
        else:
            i += 1

    return i < len(matrix) and j >= 0


matrix =[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
print(findNumberIn2DArray(matrix, 5))