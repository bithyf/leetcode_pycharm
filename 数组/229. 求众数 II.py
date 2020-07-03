"""
给定一个大小为 n 的数组，找出其中所有出现超过 ⌊ n/3 ⌋ 次的元素。

说明: 要求算法的时间复杂度为 O(n)，空间复杂度为 O(1)。
"""


def majorityElement(nums):
    num = [0, 0]
    count = [0, 0]
    for i in range(len(nums)):
        j = 0
        while j < len(num):
            if num[j] == nums[i]:
                count[j] += 1
                break
            j += 1
        if j == len(num):  # 若num中不包含nums[i]，找到count为零的下标
            j = 0
            while j < len(count):
                if count[j] == 0:
                    num[j] = nums[i]
                    count[j] += 1
                    break
                j += 1
            if j == len(count):  # 若无count为0的下标，则所有count - 1
                for j in range(len(count)):
                    count[j] -= 1
    count = [0, 0]
    for i in range(len(nums)):
        for j in range(len(num)):
            if num[j] == nums[i]:
                count[j] += 1
                break
    j = 0
    while j < len(num):
        if count[j] <= len(nums) // 3:
            del num[j]
            del count[j]
        else:
            j += 1
    return num


nums = [6, 5, 5]
print(majorityElement(nums))
