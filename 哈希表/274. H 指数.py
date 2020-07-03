def hIndex(citations) -> int:
    if len(citations) == 0:
        return 0
    citations.sort(reverse=True)
    for i in range(len(citations)):
        if citations[i] <= i + 1:
            return citations[i]