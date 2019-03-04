import heapq
class Solution(object):
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        #edge case
        if not points:
            return []
        res = []
        for point in points:
            res.append((point[0]**2 + point[1]**2, point))
        #get K largest using heap
        heapq.heapify(res)
        ans = []
        for i in range(K):
            ans.append(heapq.heappop(res)[1])
        return ans
#time: O(nlogn)
#space: O(n)
