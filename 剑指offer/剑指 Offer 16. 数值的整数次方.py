def myPow(x: float, n: int) -> float:
    tag = 0
    if n < 0:
        tag = 1
        n = -n

    def twoPow(x, n):
        if n == 0:
            return 1
        if n == 1:
            return x
        else:
            t = twoPow(x, n // 2)
            if n % 2 == 0:
                return t * t
            else:
                return t * t * x
    if tag == 0:
        return twoPow(x, n)
    else:
        return 1 / twoPow(x, n)

print(myPow(2,-2))
