class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        p2 = p3 = p5 = 0
        dp = [1]

        for i in range(1, n):
            dp.append(min(dp[p2] * 2, dp[p3] * 3, dp[p5] * 5))
            if dp[i] == dp[p2] * 2:
                p2 += 1
            if dp[i] == dp[p3] * 3:
                p3 += 1
            if dp[i] == dp[p5] * 5:
                p5 += 1

        return dp[n - 1]
