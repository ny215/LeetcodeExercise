class Solution(object):
    def minCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        size = len(costs)
        if size == 0:
            return 0
        pre = costs[0][:]
        print pre
        now =[0]*3
        print now
        for i in xrange(size -1):
            now[0] = min(pre[1], pre[2]) + costs[i+1][0]
            now[1] = min(pre[0], pre[2]) + costs[i+1][1]
            now[2] = min(pre[0], pre[1]) + costs[i+1][2]
            pre[:] = now[:]
    
        return min(pre)