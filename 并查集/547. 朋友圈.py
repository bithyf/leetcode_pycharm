def findCircleNum(self, M):
    """
    :type M: List[List[int]]
    :rtype: int
    """
    people = 0

    def dfstravel(i):
        if M[i][i] == 0:
            return
        M[i][i] = 0
        for j in range(len(M)):
            if M[i][j] == 1:
                M[i][j] = 0
                dfstravel(j)

    for p in range(len(M)):
        if M[p][p] == 1:
            people += 1
            dfstravel(p)
    return people
