class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if not s:
            return ""
        if numRows == 1:
            return s
        res = [[] * 1 for _ in xrange(numRows)]
        p = -1
        flag = 0
        for ss in s:
            if p < numRows and flag == 0:
                p += 1
                res[p].append(ss)
                if p == numRows-1:
                    flag = 1
                    continue
            if p < numRows and flag == 1:
                p -= 1
                res[p].append(ss)
                if p == 0:
                    flag = 0
                    continue
        ans = ""
        for s in res:        
            ans += "".join(s)
        return ans
            
            