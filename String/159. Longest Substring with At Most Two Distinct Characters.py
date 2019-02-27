class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        if n == 0:
            return 0
        
        start, end = 0, 0
        dic = {}
        maxLen = 0
        while end < n:
            dic[s[end]] = end
            end += 1
            if len(dic) > 2:
                delInd = min(dic.values())
                del dic[s[delInd]]
                start = delInd + 1
            
            maxLen = max(maxLen, end - start)
        return maxLen

                
            
