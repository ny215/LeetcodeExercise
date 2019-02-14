class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""
        
        check = min(strs,key = len)
        res = ""
        for i in range(len(check)):
            for string in strs:
                if check[i] != string[i]:
                    return check[:i]
        return check
                    
        