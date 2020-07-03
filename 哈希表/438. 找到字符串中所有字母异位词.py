def findAnagrams(s, p):
    index = []
    target = [0] * 26
    window = [0] * 26
    for i in range(len(p)):
        target[ord(p[i]) - 97] += 1
        window[ord(s[i]) - 97] += 1

    left = 0
    right = len(p) - 1
    window[ord(s[right]) - 97] -= 1
    while right < len(s):
        window[ord(s[right]) - 97] += 1
        if target == window:
            index.append(left)
        window[ord(s[left]) - 97] -= 1
        right += 1
        left += 1

    return index


ss = "cbaebabacd"
pp = 'abc'
print(findAnagrams(ss, pp))

