def removeDuplicates(nums):
    i = 0
    j = 1
    while j < len(nums):
        if nums[i] == nums[j]:
            while j + 1 < len(nums) and nums[j + 1] == nums[j]:
                j += 1
            if j + 1 == len(nums):
                if i != j - 1:
                    nums[i + 1] = nums[j]
                return i + 2
            nums[i + 1] = nums[j]
            nums[i + 2] = nums[j + 1]
            i += 2
            j += 2
        else:
            if i != j - 1:
                nums[i + 1] = nums[j]
            i += 1
            j += 1
    return i + 1


nums = [0, 0, 1, 1, 1, 1, 2, 3, 3]
print(removeDuplicates(nums))
