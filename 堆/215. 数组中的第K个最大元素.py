def findKthLargest(nums, k):
    r = len(nums)
    l = 0
    while True:
        num = nums[l]
        f = l
        b = r
        while f < b:
            while f < b and num > nums[b]:
                b -= 1
            if f < b:
                nums[f] = nums[b]
                f += 1
            while f < b and num < nums[f]:
                f += 1
            if f < b:
                nums[b] = nums[f]
                b -= 1
        if f == k:
            return nums[f]
        elif f > k:
            r = f - 1
        else:
            l = f + 1


