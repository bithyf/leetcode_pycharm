def isMatch(s: str, p: str) -> bool:
    i = len(s) - 1
    j = len(p) - 1

    def match(S, P, i, j):
        if i == j == -1:
            return True
        elif j == -1 and i != -1:
            return False
        elif i == -1 and j != -1:
            if j % 2 == 0:
                return False
            while j >= 0:
                if P[j] != '*':
                    return False
                j -= 2
            return True
        else:
            if P[j] != "*":
                if S[i] == P[j] or P[j] == ".":
                    return match(S, P, i - 1, j - 1)
                return False
            else:
                if P[j - 1] == S[i] or P[j] == ".":
                    return match(S, P, i - 1, j) or match(S, P, i, j - 2)
                return match(S, P, i, j - 2)

    return match(s, p, i, j)


s = "aa"
p = "a*"
isMatch(s, p)