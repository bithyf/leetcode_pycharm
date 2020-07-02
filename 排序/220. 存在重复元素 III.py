def containsNearbyAlmostDuplicate(nums, k, t):
    index_nums = [[nums[i], i] for i in range(len(nums))]
    index_nums = sorted(index_nums)
    i = 0
    while i < len(index_nums) - 1:
        width = 1
        while i + width < len(index_nums) and -t <= index_nums[i][0] - index_nums[i + width][0] <= t:
            if -k <= index_nums[i][1] - index_nums[i + width][1] <= k:
                return True
            width += 1
        i += 1
    return False


nums = [1, 5, 9, 1, 5, 9]
k = 2
t = 3
print(containsNearbyAlmostDuplicate(nums, k, t))
