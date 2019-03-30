class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        #dp[i] = min(dp[i-1], dp[i-2], dp[i-5])+1
        dp = [amount+1] * (amount+1)
        dp[0] = 0

        for i in range(1, amount+1):
            for j in range(len(coins)):
                if coins[j] <= i:
                    dp[i] = min(dp[i], dp[i-coins[j]]+1)
        if dp[-1] > amount:
            return -1
        else:
            return dp[-1]

#Time:O(S∗n)
#Space: O(S)