def generateMatrix(n):
    if n < 1:
        return []
    '''生成矩阵'''
    matrix = [[] for i in range(n)]
    for i in range(n):
        matrix[i] = [0 for i in range(n)]
    num = 0
    for k in range(n // 2):
        length = n - 2 * k - 1
        for i in range(length):
            matrix[k][k + i] = num
            num += 1
        for i in range(length):
            matrix[k + i][k + length] = num
            num += 1
        for i in range(length):
            matrix[k + length][k + length - i] = num
            num += 1
        for i in range(length ):
            matrix[k + length - i][k] = num
            num += 1
    if n % 2 != 0:
        matrix[n // 2][n // 2] = num
    return matrix
print(generateMatrix(2))