def findRepeatNumber(nums) -> int:
    i = 0
    while i < len(nums):
        if nums[i] != i:
            if nums[nums[i]] != nums[i]:
                t = nums[nums[i]]
                nums[nums[i]] = nums[i]
                nums[i] = t
            else:
                return nums[i]
        else:
            i += 1


nums = [2, 3, 1, 0, 2, 5, 3]
print(findRepeatNumber(nums))
