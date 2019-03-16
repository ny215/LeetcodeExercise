class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True
        check = {}
        for n in s:
            if n not in check:
                check[n] = 1
            else:
                del check[n]
        
        return len(check) <= 1
# time: O(n)
# space: O(n)