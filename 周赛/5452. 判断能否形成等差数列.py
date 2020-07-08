def canMakeArithmeticProgression(arr):
    arr.sort()
    i = 2
    t = arr[1] - arr[0]
    while i < len(arr):
        if arr[i] - arr[i-1] != t:
            return False
        i += 1
    return True


a = [3, 4, 1, 2]
if canMakeArithmeticProgression(a):
    print('y')
else:
    print('n')