def getLastMoment(n: int, left, right) -> int:
    max_left = max(left) if len(left) > 0 else 0
    min_right = min(right) if len(right) > 0 else n
    return max(max_left, n - min_right)
