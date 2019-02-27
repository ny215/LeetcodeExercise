class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        freq = {}
        start = 0
        maxLength = 0
        n = len(s)
        if n <= 1:
            return n
        for end in range(n):
            if s[end] in freq and start <= freq[s[end]]:
                start = freq[s[end]] + 1
            else:
                maxLength = max(maxLength, end - start + 1)
            freq[s[end]] = end
        return maxLength

                