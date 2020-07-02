def largestNumber(nums):
    if len(nums) == 0:
        return 0
    num2str = [str(num) for num in nums]
    num2str = sorted(num2str, reverse=True, key=lambda x: x[0])

    print(num2str)
    from functools import cmp_to_key

    def compare(x, y):
        if x + y < y + x:
            return 1
        return -1
    index = 0
    while index < len(num2str):
        i = 1
        while index + i < len(num2str) and num2str[index][0] == num2str[index + i][0]:
            i += 1
        if i != 1:
            num2str[index: index + i] = sorted(num2str[index: index + i], key=cmp_to_key(compare))
        index += i
    i = 0
    while i < len(num2str) - 1 and num2str[i] == '0':
        del num2str[i]
    return ''.join(num2str)


nums = [0, 0]
# nums[1:3] = [1, 2]
# print(nums)
print(largestNumber(nums))
# print('32' + '33')
