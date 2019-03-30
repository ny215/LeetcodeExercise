class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        minprice = float('inf')
        maxprofit = 0
        for p in prices:
            minprice = min(minprice, p)
            maxprofit = max(maxprofit, p - minprice)
        return maxprofit