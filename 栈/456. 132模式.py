"""
给定一个整数序列：a1, a2, ..., an，
一个132模式的子序列 ai, aj, ak 被定义为：当 i < j < k 时，ai < ak < aj。
设计一个算法，当给定有 n 个数字的序列时，验证这个序列中是否含有132模式的子序列。

"""


def find132pattern(nums):
    stack = []
    premin = []
    for num in nums:
        if len(premin) == 0 or num < premin[-1]:
            premin.append(num)
        else:
            premin.append(premin[-1])

    for index in range(len(nums)-1, -1, -1):
        if nums[index] > premin[index]:
            while len(stack) > 0 and stack[-1] < nums[index]:
                if premin[index] < stack[-1]:
                    return True
                stack.pop()
            stack.append(nums[index])
    return False