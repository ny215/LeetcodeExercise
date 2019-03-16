class Solution(object):
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        lo = 0
        hi = len(A) -1
        while lo < hi:
            mid = (hi + lo) /2
            if A[mid] < A[mid+1]:
                lo = mid + 1
            else:
                hi = mid
        return lo
# time: O(logn)
# space: O(1)