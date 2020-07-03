def replaceSpace(s) -> str:
    list_s = list(s)
    for i in range(len(list_s)):
        if list_s[i] == ' ':
            list_s[i] = '%20'
    return "".join(list_s)