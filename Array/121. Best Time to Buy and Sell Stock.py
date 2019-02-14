class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        maxProfit = 0
        currMin = float('inf')
        for i in range(len(prices)):
            if prices[i] < currMin:
                currMin = prices[i]
            elif (prices[i] - currMin) > maxProfit: 
                maxProfit = prices[i] - currMin
        return maxProfit
