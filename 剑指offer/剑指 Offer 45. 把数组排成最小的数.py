class Solution(object):
    def minNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        from functools import cmp_to_key
        def compare(a, b):
            if a + b > b + a:
                return 1
            return -1

        for i in range(len(nums)):
            nums[i] = str(nums[i])

        nums.sort(key=cmp_to_key(compare))
        return ''.join(nums)
