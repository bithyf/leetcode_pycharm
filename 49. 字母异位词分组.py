
def groupAnagrams(strs):
    values = dict()
    for s in strs:
        # key = ''.join(sorted(s))
        key = sorted(s)
        if key in values:
            values[key].append(s)
        else:
            values[key] = [s]
    return list(values.values())


test = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(groupAnagrams(test))