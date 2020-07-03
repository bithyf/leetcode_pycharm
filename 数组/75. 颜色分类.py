def sortColors(nums):
    i = 0     # 0的位置
    j = len(nums) - 1  # 2的位置
    k = 0
    while k <= j:
        if nums[k] == 0 and k > i:
            nums[k] = nums[i]
            nums[i] = 0
            i += 1
        elif nums[k] == 2 and k < j:
            nums[k] = nums[j]
            nums[j] = 2
            j -= 1
        else:
            k += 1


nums = [2, 0, 2, 1, 1, 0]
sortColors(nums)
print(nums)
