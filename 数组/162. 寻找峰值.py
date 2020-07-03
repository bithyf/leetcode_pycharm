"""
峰值元素是指其值大于左右相邻值的元素。

给定一个输入数组 nums，其中 nums[i] ≠ nums[i+1]，找到峰值元素并返回其索引。

数组可能包含多个峰值，在这种情况下，返回任何一个峰值所在位置即可。

"""


def findPeakElement(nums):
    pa = 0
    pb = len(nums)
    while pa < pb:
        pm = (pa + pb) // 2
        if nums[pm + 1] < nums[pm]:
            pb = pm
        else:
            pa = pm + 1
    return pa


test = [1, 2, 3, 1]
print(findPeakElement(test))
