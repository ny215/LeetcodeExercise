class Solution(object):
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """

        n = len(A)
        res = []
        pos, neg = 0, 0
        while pos < n and A[pos] < 0:
            pos += 1
        neg = pos - 1
        while 0 <= neg and pos < n:
            if A[neg]**2 <= A[pos] **2:
                res.append(A[neg]**2)
                neg -= 1
            else:
                res.append(A[pos]**2)
                pos += 1
                
        while pos < n:
            res.append(A[pos]**2)
            pos += 1
        while neg >= 0:
            res.append(A[neg]**2)
            neg -= 1
            
        return res

# time: O(n)
# space: O(n)