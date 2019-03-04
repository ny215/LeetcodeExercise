class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        parent = range(n)
        rank =[0] * n
        
        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            xr, yr = find(x), find(y)
            if xr == yr:
                return False
            elif rank[xr] < rank[yr]:
                parent[xr] = yr
            elif rank[yr] < rank[xr]:
                parent[yr] = xr
            else:
                parent[yr] = xr
                rank[xr] += 1
            return True
        

        for i, j in edges:
            union(i, j)
        res = set()
        for p in parent:
            res.add(find(p))
        return len(res)