def cuttingRope(self, n: int) -> int:
    if n <= 3:
        return n - 1
    length = n // 3
    left = n % 3

    if left == 0:
        return pow(3, length)
    if left == 1:
        return pow(3, length - 1) * 4
    else:
        return pow(3, length) * 2