class Solution(object):
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        if not N:
            return 0
        dp = [0 for _ in xrange(N+1)]
        dp[0] = 0
        dp[1] = 1
        for i in range(2, N+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[-1]


#time: O(n)
#space: O(n)