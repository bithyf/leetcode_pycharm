def partitionLabels(S):
    loc = {}
    for i in range(len(S)):
        if S[i] not in loc:
            loc[S[i]] = [i, i]
        else:
            loc[S[i]][1] = i
    key = []
    i = 0
    while i < len(S):
        start = i
        maxlen = loc[S[i]][1]
        while i < maxlen:
            maxlen = max(maxlen, loc[S[i]][1])
            if maxlen == len(S) - 1:
                key.append(len(S) - start)
                return key
            i += 1
        i += 1
        key.append(i - start)
    return key


S = 'acbcb'
print(partitionLabels(S))