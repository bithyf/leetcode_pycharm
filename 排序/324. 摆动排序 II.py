def wiggleSort(nums) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    nums.sort()

    mid = len(nums)//2 + len(nums)%2
    nums[0:mid] = reversed(nums[0:mid])
    nums[mid:] = reversed(nums[mid:])

    front = 1
    back = mid
    while back < len(nums):
        num = nums[back]
        del nums[back]
        nums.insert(front, num)
        back += 1
        front += 2
    print(nums)




nums = [1,5,1,1,6,4]
wiggleSort(nums)