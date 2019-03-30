class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        if not s or not p:
            return []
        res = []
        dicp = [0] * 26
        dics = [0] * 26
        count = 0
        for i in range(len(p)):
            dicp[ord(p[i]) - ord('a')] += 1
        for i in range(len(s)):
            count += 1
            dics[ord(s[i]) - ord('a')] += 1
            if count == len(p):
                if dics == dicp:
                    res.append(i-len(p)+1)
                dics[ord(s[i-len(p)+1]) - ord('a')] -= 1
                count -= 1
        return res

#space: O(n)
#time: O(n)