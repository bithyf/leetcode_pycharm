def numSubmat(mat) -> int:
    import sys
    left = []
    ans = 0
    for i in range(len(mat)):
        now = 0
        left.append([])
        for j in range(len(mat[0])):
            if mat[i][j] == 1:
                now += 1
            else:
                now = 0
            left[i].append(now)
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            minnum = sys.maxsize
            for k in range(i, -1, -1):
                minnum = min(left[k][j], minnum)
                if minnum == 0:
                    break
                ans += minnum
    return ans


matr = [[1, 1, 1, 1, 0], [1, 0, 0, 1, 0], [0, 0, 1, 0, 1], [0, 1, 0, 0, 0]]
print(numSubmat(matr))
