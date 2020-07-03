# 给定一个整数数组 nums ，找出一个序列中乘积最大的连续子序列（该序列至少包含一个数）。
def maxProduct(nums):
    maxnum = nums[0]
    minnum = 1
    cur = 1
    for i in range(len(nums)):
        maxnum = nums[0]
        minnum = 1
        cur = 1
        for i in range(len(nums)):
            if nums[i] < 0:
                minnum, cur = cur, minnum
            cur = max(cur * nums[i], nums[i])
            minnum = min(minnum * nums[i], nums[i])
            maxnum = max(maxnum, cur)
    return maxnum


nums = [-4,-3,-2]
print(maxProduct((nums)))

