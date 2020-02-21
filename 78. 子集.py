def subsets(nums):
    dlr = [[]]

    for i in range(len(nums)):
        for num in range(len(dlr)):
            dlr.append(dlr[num] + [nums[i]])


    # def backtracking(i, num):
    #     if i == len(nums):
    #         dlr.append(num)
    #     else:
    #         backtracking(i + 1, num[:])
    #         num.append(nums[i])
    #         backtracking(i + 1, num[:])
    #
    # backtracking(0, [])
    print(dlr)

nums = [1, 2, 3]
subsets(nums)

