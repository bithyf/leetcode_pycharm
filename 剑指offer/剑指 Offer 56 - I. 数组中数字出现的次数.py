class Solution(object):
    def singleNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        from functools import reduce
        ret = reduce(lambda x, y: x ^ y, nums)
        div = 1
        while ret & div == 0:
            div <<= 1

        a = 0
        b = 0
        for num in nums:
            if num & div == 0:
                a ^= num
            else:
                b ^= num

        return [a, b]
