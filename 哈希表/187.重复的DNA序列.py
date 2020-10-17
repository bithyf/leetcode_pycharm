def findRepeatedDnaSequences(s: str):
    L, length = 10, len(s)
    if length < 10:
        return None
    project = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
    num = list(map(lambda x: project[x], s))
    seen, out = set(), []
    h = 0
    for i in range(length - L + 1):
        if i == 0:
            for j in range(L):
                h = h * 4 + num[j]
        else:
            h = h * 4 - num[i - 1] * pow(4, L) + num[i + L - 1]
        if h in seen:
            out.append(s[i:i + L])
        seen.add(h)
    return list(set(out))






string = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
print(findRepeatedDnaSequences(string))


