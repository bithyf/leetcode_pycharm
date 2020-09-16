def lengthOfLongestSubstring(s: str) -> int:
    if len(s) < 2:
        return len(s)
    maxlength = 0
    left = right = 0
    for n in s:
        # 若n不在字符串里窗口大小加一
        if n not in s[left:right]:
            right += 1
            if right - left > maxlength:
                maxlength += 1
        else:
            left += s[left:right].index(n) + 1
            right += 1

    return maxlength


S = "bbtablud"
print(lengthOfLongestSubstring(S))

