class Solution(object):
    def verifyPostorder(self, postorder):
        """
        :type postorder: List[int]
        :rtype: bool
        """

        def visit(nums):
            if len(nums) <= 1:
                return True
            for idx, in enumerate(nums):
                if nums[idx] > nums[-1]:
                    break
            if nums[-1] > min(nums[idx:]):
                return False
            return visit(nums[:idx]) and visit(nums[idx: -1])

        return visit(postorder)


for i in range(10):
    pass
print(i)
