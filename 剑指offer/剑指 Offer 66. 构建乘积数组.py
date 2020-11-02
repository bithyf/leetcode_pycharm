class Solution(object):
    def constructArr(self, a):
        """
        :type a: List[int]
        :rtype: List[int]
        """
        b = [1]
        for num in a[:-1]:
            b.append(b[-1] * num)
        tmp = 1
        length = len(a)
        for i in range(length - 1):
            tmp *= a[length - 1 - i]
            b[length - 1 - i - 1] *= tmp
        return b
