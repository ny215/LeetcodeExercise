class Solution(object):
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        inc = True
        dec = True
        
        for i in range(len(A)-1):
            if A[i] < A[i+1]:
                dec = False
            elif A[i] > A[i+1]:
                inc = False
        return inc or dec


# time: O(n)
# space: O(1)