class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix or not matrix[0]:
            return []
        res = []
        m = len(matrix)
        n = len(matrix[0])
        u, d, l, r = 0, m-1, 0, n-1
        while l < r and u < d:
            res.extend([matrix[u][j] for j in xrange(l, r)])
            res.extend([matrix[i][r] for i in xrange(u, d)])
            res.extend([matrix[d][j] for j in xrange(r, l,-1)])
            res.extend([matrix[i][l] for i in xrange(d, u, -1)])
            u += 1
            d -= 1
            l += 1
            r -= 1
        if l == r:
            res.extend([matrix[i][r] for i in xrange(u, d+1)])
        elif u == d:
            res.extend([matrix[u][j] for j in xrange(l, r+1)])
        return res

#time: O(n)
#space: O(n)