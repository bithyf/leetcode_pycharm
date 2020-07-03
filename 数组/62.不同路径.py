def uniquePaths(m, n):
    num1 = 1
    num2 = 1
    for i in range(m - 1):
        num1 *= (m + n - 2 - i)
        num2 *= i + 1
    return num1 // num2


print(uniquePaths(3, 2))