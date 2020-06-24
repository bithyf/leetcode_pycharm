def leastInterval(tasks, n):
    from collections import Counter
    count = Counter(tasks)
    print(count.most_common(1))
    # count = sorted(count.items(), reverse=True, key=lambda x: x[1])


tasks = ["A", "A", "A", "B", "B", "B", "C", "C"]
n = 2
leastInterval(tasks, n)

a = [1,2,3,4,5,5]
print(a.count(5))