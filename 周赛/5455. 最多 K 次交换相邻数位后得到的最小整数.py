def minInteger(num: str, k: int) -> str:
    i = 1
    while i < len(num):
        if num[i] < num[i - 1]:
            break
        i+=1
    if i >= len(num):
        return num
    num = list(num)
    start = 0
    while k > 0 and start < len(num):

        # index = num.index(min(num[start:]), start)
        # if k < index - start:
        #     print("start: ",start)
        #     print("start + k + 1:",start + k + 1)
        index = num.index(min(num[start: min(start + k + 1, len(num))]), start, min(start + k + 1, len(num)))

        num.insert(start, num[index])
        del num[index + 1]
        k -= (index - start)
        start += 1

    return ''.join(num)
    pass

nums = '4132'

k = 2
print(minInteger(nums, k))
