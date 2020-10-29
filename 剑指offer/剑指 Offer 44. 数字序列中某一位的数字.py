class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 10:
            return n

        num = 90
        length = 2
        index = 9
        start = 1
        while True:
            index += num * length
            if index >= n:
                break
            length += 1
            num *= 10
        index -= num * length
        left = n - index
        start = num // 9 - 1
        if left % length == 0:
            targetNum = start + left / length
            # print(targetNum)
            return int(str(targetNum)[-1])
        else:
            targetNum = start + left // length + 1
            # print(targetNum)
            return int(str(targetNum)[left % length - 1])
       