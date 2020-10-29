class Solution(object):
    def translateNum(self, num):
        """
        :type num: int
        :rtype: int
        """
        num = str(num)
        q = 0
        r = 1
        for i in range(1, len(num)):
            if '10' < num[i - 1] + num[i] < '26':
                p = r
                r = r + q
                q = p
            else:
                q = r

        return r
