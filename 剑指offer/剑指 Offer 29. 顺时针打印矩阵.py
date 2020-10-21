class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        nums = []
        row = len(matrix)
        col = len(matrix[0])
        i = 0
        while i < (min(row, col) + 1) // 2:
            for j in range(i, col - i):
                nums.append(matrix[i][j])
            for j in range(i + 1, row - i):
                nums.append(matrix[j][col - i - 1])
            for j in range(col - i - 2, i - 1, -1):
                nums.append(matrix[row - i - 1][j])
            for j in range(row - i - 2, i, -1):
                nums.append(matrix[j][i])
            i += 1
        return nums
