class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        curr = [1] * (rowIndex + 1)
        for i in range(1, rowIndex+1):
            for j in range(i-1, 0, -1):
                curr[j] += curr[j-1]
                print curr
        return curr
    
