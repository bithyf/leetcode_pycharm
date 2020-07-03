"""
假设按照升序排序的数组在预先未知的某个点上进行了旋转。

( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。

请找出其中最小的元素。

你可以假设数组中不存在重复元素。
"""


def findMin(nums):
    pb = len(nums) - 1
    pa = 0
    while pa <= pb:
        pm = (pa + pb) // 2
        if nums[pb] >= nums[pa]:
            return nums[pa]
        elif nums[pm] >= nums[pa]:
            pa = pm + 1
        else:
            pb = pm


nums = [4, 5, 6, 7, 0, 1, 2]
print(findMin(nums))
