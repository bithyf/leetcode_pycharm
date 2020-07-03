def topKFrequent(nums, k):
    seen = dict()
    for i in range(len(nums)):
        if nums[i] in seen:
            seen[nums[i]] += 1
        else:
            seen[nums[i]] = 1
    first = second = None
    for key in seen:
        if first is None or seen[key] > seen[first]:
            first = key
            continue
        if second is None or seen[key] > seen[second]:
            second = key
    return [first, second]


nums = [5, 5, 5, 4, 4, 7, 7]
k = 2
print(topKFrequent(nums, k))
