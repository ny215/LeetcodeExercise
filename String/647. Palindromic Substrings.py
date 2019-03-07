class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        res = 0
        for i in range(2*n -1):
            l = i /2
            r = l + i%2
            while  0 <= l and r < n and s[l] == s[r]:
                l -= 1
                r += 1
                res += 1
        return res


#time: O(n2)
#space: O(1)