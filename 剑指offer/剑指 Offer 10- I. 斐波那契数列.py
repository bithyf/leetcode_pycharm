def fib(n: int) -> int:
    f = [0, 1]
    i = 2
    while i <= n:
        f.append(f[i - 1] + f[i - 2])
        i += 1
    print(f)
    return f[n]

print(fib(45))
