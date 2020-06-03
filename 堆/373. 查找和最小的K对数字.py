def kSmallestPairs(nums1, nums2, k: int):
    if len(nums2) <= 1:
        return []
    indexs = [[i, 0] for i in range(len(nums1))]
    keys = []
    while len(keys) < k and len(indexs) > 0:
        keys.append([nums1[indexs[0][0]], nums2[indexs[0][1]]])
        if indexs[0][1] == len(nums2) - 1:
            del (indexs[0])
            continue

        indexs[0][1] += 1
        i = 1
        while i < len(indexs):
            if nums1[indexs[0][0]] + nums2[indexs[0][1]] < nums1[indexs[i][0]] + nums2[indexs[i][1]]:
                break
            i += 1
        indexs.insert(i, indexs[0])
        del indexs[0]

    return keys

    return keys


n1 = [1, 1, 2]
n2 = [1, 2, 3]
print(kSmallestPairs(n1, n2, 2))