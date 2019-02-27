class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        n = len(s)
        if n == 0 or k == 0:
            return 0
        
        start, end = 0, 0
        dic = {}
        maxLen = 0
        while end < n:
            # add new character and move right pointer
            
            dic[s[end]] = end
            end += 1
            if len(dic) > k:
                delInd = min(dic.values())
                del dic[s[delInd]]
                start = delInd + 1
            
            maxLen = max(maxLen, end - start)
        return maxLen

                