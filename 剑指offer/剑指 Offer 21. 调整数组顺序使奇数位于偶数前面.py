def exchange(nums):
    if len(nums) == 0:
        return nums
    f = 0
    b = len(nums) - 1
    t = nums[0]
    while f < b:
        while f < b and nums[b] % 2 == 0:
            b -= 1
        nums[f] = nums[b]
        while f < b and nums[f] % 2 == 1:
            f += 1
        nums[b] = nums[f]
    nums[f] = t

    return nums