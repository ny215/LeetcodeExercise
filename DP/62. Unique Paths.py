class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        #dp[i][j] = dp[i-1][j] + dp[i][j-1]
        if not m or not n:
            return 0
        dp = [[0]* n for _ in xrange(m)]
        for j in range(n):
            dp[0][j] = 1
        for i in range(m):
            dp[i][0] = 1
        for i in range(1, m):
            for j in range(1,n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]

#time: O(m*n)
#space: O(m*n)