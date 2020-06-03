def kthSmallest(matrix, k):
    """
    :type matrix: List[List[int]]
    :type k: int
    :rtype: int
    """
    klist = []
    for elem in matrix:
        klist += elem
    import heapq
    key = heapq.nsmallest(k, klist)[-1]

    return key