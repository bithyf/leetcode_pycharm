"""
给定一个无重复元素的有序整数数组，返回数组区间范围的汇总。
"""


def summaryRanges(nums):
    spams = []
    i = 0
    while i < len(nums):
        spam = str(nums[i])
        j = 1
        while i + j < len(nums) and nums[i] + j == nums[i + j]:
            j += 1
        if j != 1:
            spam += '->' + str(nums[i + j - 1])
        i += j
        spams.append(spam)
    return spams


nums = [0, 1, 2, 4, 5, 7]
print(summaryRanges(nums))
