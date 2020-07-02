def pancakeSort(A):
    reverse_array = []
    pos = len(A) - 1
    while pos >= 0:
        index = 0
        for i in range(pos + 1):
            if A[i] > A[index]:
                index = i
        A[0:index + 1] = reversed(A[0:index + 1])
        reverse_array.append(index + 1)
        A[0:pos + 1] = reversed(A[0:pos + 1])
        reverse_array.append(pos + 1)
        pos -= 1
    return reverse_array


a = [3,2,4,1]

print(pancakeSort(a))

