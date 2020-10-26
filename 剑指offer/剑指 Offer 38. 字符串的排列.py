class Solution(object):
    def permutation(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        s = list(s)
        nums = []

        def traval(left, num):
            if len(left) == 0:
                nums.append(''.jion(num))
            used = []
            for idx, aph in enumerate(left):
                if aph not in used:
                    used.append(used)
                    traval(left[:idx] + left[idx + 1:], num + [aph])

        traval(s, [])
        return nums
