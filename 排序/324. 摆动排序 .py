def wiggleSort(nums) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    front = 0
    back = len(nums) - 1
    midnum = nums[0]
    midindex = 0
    while midindex != len(nums) // 2:
        while True:
            while front < back and nums[back] >= midnum:
                back -= 1
            nums[front] = nums[back]
            if back == front:
                break
            front += 1
            while front < back and nums[front] <= midnum:
                front += 1
            nums[back] = nums[front]
            if back == front:
                break
            back -= 1
        nums[front] = midnum
        midindex = back
        if midindex < len(nums) // 2:
            back = len(nums) - 1
            front = midindex + 1
        elif midindex > len(nums) // 2:
            back = midindex - 1
            front = 0
        midnum = nums[front]
    if len(nums) % 2 != 0:
        midindex += 1
    index = 0
    for i in range(midindex):
        if nums[i] == midnum:
            nums[i], nums[index] = nums[index], nums[i]
            index += 1
    i = len(nums) - 1
    index = len(nums) - 1
    while i >= midindex:
        if nums[i] == midnum:
            nums[i], nums[index] = nums[index], nums[i]
            index -= 1
        i -= 1

    front = 1
    back = midindex
    while back < len(nums):
        num = nums[back]
        del nums[back]
        nums.insert(front, num)
        back += 1
        front += 2

    print(nums)


nums = [1, 4, 6, 4]

wiggleSort(nums)
