def minArray(numbers) -> int:
    l = 0
    r = len(numbers) - 1
    while l < r:
        if numbers[l] < numbers[r]:
            return numbers[l]
        while l < r and numbers[l] == numbers[r]:
            l += 1
            r -= 1
        mid = (l + r) // 2
        if numbers[mid] >= numbers[l]:
            l = mid + 1
        else:
            r = mid - 1
    return numbers[r]
