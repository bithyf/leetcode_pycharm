def subsetsWithDup(nums):
    dkr = [[]]
    nums = sorted(nums)
    # 存放加入上一个数后，新增的数组
    for i in range(len(nums)):
        if i != 0 and nums[i] == nums[i - 1]:
            q = len(dkr)
            dkr += [dkr[num] + [nums[i]] for num in range(p, len(dkr))]
            p = q
        else:
            p = len(dkr)
            dkr += [dkr[num] + [nums[i]] for num in range(len(dkr))]
    return dkr


n = [1, 2, 2]
print(subsetsWithDup(n))

