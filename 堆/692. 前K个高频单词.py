def topKFrequent(words, k):
    import collections
    import heapq
    count = collections.Counter(words)
    heap = [(-freq, word) for word, freq in count.items()]
    heapq.heapify(heap)
    print(heap)
    return [heapq.heappop(heap)[1] for _ in range(k)]


test = ["i", "love", "leetcode", "i", "love", "coding"]
print(topKFrequent(test, 2))
