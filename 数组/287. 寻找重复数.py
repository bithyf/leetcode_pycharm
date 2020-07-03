"""
给定一个包含 n + 1 个整数的数组 nums，其数字都在 1 到 n 之间（包括 1 和 n），
可知至少存在一个重复的整数。
假设只有一个重复的整数，找出这个重复的数。

"""


def findDuplicate(nums):
    low = 1
    high = len(nums) - 1
    while low < high:
        left = right = 0
        mid = (low + high) // 2
        for i in range(len(nums)):
            if low <= nums[i] <= mid:
                left += 1
            elif mid < nums[i] <= high:
                right += 1
        if high - mid < right:
            low = mid + 1
        else:
            high = mid
    return low


# 快慢针
# kuaimanzhe
# def findDuplicate(nums):
#     fast = 0
#     slow = 0
#     while True:
#         fast = nums[nums[fast]]
#         slow = nums[slow]
#         if fast == slow:
#             break
#     finder = 0
#     while finder != slow:
#         slow = nums[slow]
#         finder = nums[finder]
#     return finder


inp = [1, 3, 4, 2, 1]
print(findDuplicate(inp))
