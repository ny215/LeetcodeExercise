from collections import deque
class Solution(object):
    def shortestDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return -1

        row = len(grid)
        col = len(grid[0])
        hit = [[0]* col for _ in xrange(row)]
        dist =[[0]* col for _ in xrange(row)]
        building = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    building += 1

        def bfs(i,j):
            visited = [[False]* col for _ in xrange(row)]
            visited[i][j] = True
            count1 = 1
            queue = deque([])
            queue.append((i,j,0))
            directions = [(1,0),(-1,0),(0,1),(0,-1)]
            while queue:
                i, j, depth = queue.popleft()
                for d in directions:
                    x = i + d[0]
                    y = j + d[1]
                    if 0<=x < row and 0 <= y < col and visited[x][y] == False:
                        visited[x][y] = True
                        if grid[x][y] == 0:
                            queue.append((x,y,depth+1))
                            hit[x][y] += 1
                            dist[x][y] += depth+1
                        elif grid[x][y] == 1:
                            count1 += 1
            return count1 == building
            
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    if not bfs(i,j):
                        return -1
        mini = float('inf')
        print dist
        for i in range(row):
            for j in range(col):
                if dist[i][j]  and hit[i][j] == building:
                    mini = min(mini, dist[i][j])
        if mini == float('inf'):
            return -1
        else:
            return mini


        

        