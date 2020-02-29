"""
给定长度为 n 的整数数组 nums，其中 n > 1，返回输出数组 output ，
其中 output[i] 等于 nums 中除 nums[i] 之外其余各元素的乘积。

"""


def productExceptSelf(nums):
    output = [1]
    for i in range(1, len(nums)):
        output.append(output[i - 1] * nums[i - 1])
    left = 1
    for i in range(len(nums) - 2, -1, -1):
        left *= nums[i + 1]
        output[i] *= left
    return output


input = [1, 2, 3, 4]
print(productExceptSelf(input))
