def numSub(self, s: str) -> int:
    num = 0
    i = 0
    while i < len(s):
        length = 0
        while s[i] == '0':
            i += 1
        while s[i] == '1':
            length += 1
            i += 1
        num += ((length + 1) * length) // 2
        num %= 1000000007

    return num