def decodeString(s: str):
    left = []
    answer = list(s)
    i = 0
    while i < len(answer):
        if answer[i] == '[':
            left.append(i)
            i += 1
        elif answer[i] == ']':
            index = left.pop()
            j = index - 1
            loop = ''
            while  j >= 0 and '0' <= answer[j] <= '9':
                loop = answer[j] + loop
                j -= 1

            loop = int(loop)
            answer = answer[0:index - 1] + answer[index + 1:i] * loop + answer[i + 1:]
            i = i + 1 - 2 - (index - j) + (i - index - 1) * (loop - 1)
        else:
            i += 1
    return ''.join(answer)


# s = "10[a]"
# decodeString(s)
s = '123'
print(s[0:1])