def numIdenticalPairs(nums) -> int:
    from collections import Counter
    nums = Counter(nums)
    # print(nums)
    pair = 0
    for key in nums:
        if nums[key] >= 2:
            pair += (nums[key] * (nums[key] - 1)) // 2
    return pair


nums = [1, 2, 3, 1, 1, 3]
print(numIdenticalPairs(nums))
