def findLongestWord(s,  d) -> str:
    d = sorted(d, key=lambda x: [-len(x), x])

    for alpha in d:
        i = 0
        for alp in s:
            if alp == alpha[i]:
                i += 1
                if i == len(alpha):
                    return alpha


s = "abpcplea"
d = ["ble","app","monkey","plea"]
print(findLongestWord(s, d))

