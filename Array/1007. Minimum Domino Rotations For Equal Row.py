class Solution(object):
    def minDominoRotations(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        if not A or not B:
            return -1
        n = len(A)
        counter = {}
        for i in range(n):
            if A[i] not in counter:
                counter[A[i]] = 1
            else:
                counter[A[i]] += 1
            if B[i] not in counter:
                counter[B[i]] = 1
            else:
                counter[B[i]] += 1
        maxnum = max(counter, key=counter.get)
        freq = max(counter.values())
        if freq < n :
            return -1
        same = 0
        maxA = 0
        maxB = 0
        for i in range(n):
            if A[i] != maxnum and B[i] != maxnum:
                return -1
            if (A[i] == maxnum and B[i] == maxnum):
                    same += 1
            if A[i] == maxnum:
                maxA += 1
            if B[i] == maxnum:
                maxB += 1
        return min(maxA, maxB) - same
