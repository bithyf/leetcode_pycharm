def numWays(n: int) -> int:
    f0 = 1
    f1 = 1
    i = 2
    while i <= n:
        t = f1
        f1 += f0
        f0 = t
        i += 1
    return f1

print(numWays(2))