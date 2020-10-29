class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        s_index = {}
        length = 0
        maxLength = length
        for i in range(len(s)):
            if s[i] not in s_index:
                s_index[s[i]] = i
                length += 1
            else:
                length += (min(s_index[s[i]] - i, length[-1] + 1))
                s_index[s[i]] = i
            if maxLength < length:
                maxLength = length
        return maxLength
