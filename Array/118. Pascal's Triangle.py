class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        triangle = []
        for i in range(1, numRows+1):
            triangle.append([1]*i)
        for i in range(2, numRows):
            for j in range(1,len(triangle[i-1])):
                triangle[i][j] = triangle[i-1][j-1] + triangle[i-1][j]
        return triangle