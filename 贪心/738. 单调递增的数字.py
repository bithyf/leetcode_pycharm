def monotoneIncreasingDigits(N: int):
    if N == 0:
        return 0
    num = []
    while N is not 0:
        num.append(N % 10)
        N = N // 10
    num.reverse()
    i = 1
    while i < len(num):
        if num[i] < num[i - 1]:
            if i == len(num):
                break
            right = 0
            while i + right < len(num):
                num[i + right] = 9
                right += 1
            left = 1
            while i - left - 1 >= 0 and num[i - left] == num[i - left - 1]:
                num[i - left] = 9
                left += 1
            num[i - left] -= 1

        i += 1

    return int(''.join([str(n) for n in num]))


print(monotoneIncreasingDigits(332))
# a = [1,2,3,4]
# print(str(a))
