def wiggleMaxLength(nums) -> int:
    length = 1

    i = 0
    while i + 1 < len(nums) and nums[i] == nums[i + 1]:
        i += 1
    if i + 1 == len(nums):
        return 1
    i += 1
    tag = nums[i - 1] - nums[i]
    while i < len(nums):
        if tag < 0:
            while i < len(nums) and nums[i] >= nums[i - 1]:
                i += 1
            length += 1
            tag = -tag
        else:
            while i < len(nums) and nums[i] <= nums[i - 1]:
                i += 1
            length += 1
            tag = -tag
    return length
