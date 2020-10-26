class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        vote = 0
        major = 0
        for num in nums:
            if num == major:
                vote += 1
            else:
                if vote == 0:
                    major = num
                    vote = 1
                else:
                    vote -= 1
        return major
