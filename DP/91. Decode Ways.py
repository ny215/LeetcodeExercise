class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        #dp[i] = dp[i-1] if s[i] != 0 + dp[i-2] if '09' < s[i-1:i+1] < '27'
        if not s:
            return 0
        n = len(s)
        dp =[0 for _ in xrange(n+1)]
        dp[0] = 1
        for i in range(1, n+1):
            if s[i-1] != '0':
                dp[i] += dp[i-1]
            if i != 1 and '09' < s[i-2:i] < '27':
                dp[i] += dp[i-2]
        return dp[-1]
            