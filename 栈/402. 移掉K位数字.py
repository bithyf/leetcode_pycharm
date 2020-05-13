"""
给定一个以字符串表示的非负整数 num，移除这个数中的 k 位数字，使得剩下的数字最小。
"""


def removeKdigits(num: str, k: int):
    key = list(num)
    stack = []
    count = 0
    for i in range(len(key)):
        if len(stack) > 0:
            if num[i] < stack[-1]:
                stack.pop()
                count += 1
                if count == k:
                    break
        stack.append(num[i])
    key = stack + key[i:]
    while key[i] is not 0 and len(key) > 1:
        del key[i]
    return ''.join(key)

