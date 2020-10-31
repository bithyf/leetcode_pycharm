class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2:
            return 0
        minNum = prices[0]
        maxP = 0
        for price in prices:
            if price <= minNum:
                minNum = price
            else:
                maxP = max(maxP, price - minNum)
        return maxP
