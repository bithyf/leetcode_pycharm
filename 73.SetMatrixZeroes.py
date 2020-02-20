"""
Given a m x n matrix, if an element is 0, set its entire row and column to 0.
 Do it in-place.
"""


def setZeroes(matrix):
    tagx = [0 for i in range(len(matrix))]
    tagy = [0 for i in range(len(matrix[0]))]
    for i in range(len(tagx)):
        for j in range(len(tagy)):
            if matrix[i][j] == 0:
                tagx[i] = 1
                tagy[j] = 1

    for i in range(len(tagx)):
        if tagx[i] == 1:
            for j in range(len(tagy)):
                matrix[i][j] = 0

    for i in range(len(tagy)):
        if tagy[i] == 1:
            for j in range(len(tagx)):
                matrix[j][i] = 0


matrix = [
    [0, 1, 2, 0],
    [3, 4, 5, 2],
    [1, 3, 1, 5]
]
setZeroes(matrix)
print(matrix)