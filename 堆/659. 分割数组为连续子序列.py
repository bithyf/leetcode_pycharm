def isPossible(nums):
    i = 0
    nums1 = []
    while i < len(nums):
        count = 1
        while i + count < len(nums) and nums[i] == nums[i + count]:
            count += 1
        nums1.append([nums[i], count])
        i += count
    print(nums1)

    while True:
        length = 1
        i = 0
        while i < len(nums1) and nums1[i][1] == 0:
            i += 1
        if i == len(nums1):
            return True
        nums1[i][1] -= 1
        while i + 1 < len(nums1) and nums1[i][0] + 1 == nums1[i + 1][0]:
            if nums1[i][1] + 1 > nums1[i + 1][1]:
                break
            nums1[i + 1][1] -= 1
            length += 1
            i += 1
        if length < 3:
            return False


num = [1, 2, 3,  4, 5, 5, 6]
print(isPossible(num))
