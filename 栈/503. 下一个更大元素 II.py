"""
给定一个循环数组（最后一个元素的下一个元素是数组的第一个元素），
输出每个元素的下一个更大元素。数字 x 的下一个更大的元素是按数组
遍历顺序，这个数字之后的第一个比它更大的数，这意味着你应该循环地
搜索它的下一个更大的数。如果不存在，则输出 -1。
 """


def nextGreaterElements(nums):
    length = len(nums)
    if length == 0:
        return []
    stack = []
    next = [-1] * length
    for i in range(length):
        while len(stack) > 0 and nums[stack[-1]] < nums[i]:
            next[stack[-1]] = nums[i]
            stack.pop()
        stack.append(i)
    for i in range(stack[-1]):
        while len(stack) > 0 and nums[stack[-1]] < nums[i]:
            next[stack[-1]] = nums[i]
            stack.pop()
    return next


