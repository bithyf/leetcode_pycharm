def reorganizeString(S):
    import collections
    count = collections.Counter(S)
    count = sorted(count.items(), key=lambda x: x[1], reverse=True)
    max_num = count[0][1]
    print(max_num)
    if max_num > (len(S) % 2 + len(S)) // 2:
        return ""

    key = ['']*len(S)
    i = 0
    for letter in count:
        for num in range(letter[1]):
            key[i] = letter
            i += 2
            if i >= len(S):
                i = 1
    key2s = ''.join(key)
    return key2s

