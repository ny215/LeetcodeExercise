#DFS recursion
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0
        count = 0
        row = len(grid)
        col = len(grid[0])
        for i in range(row):
            for j in range(col):
                if grid[i][j] == "1":
                    count += 1
                    self.sink(grid, i, j)
        return count
    
    def sink(self, grid, i, j):
        if i < 0 or i >= len(grid):
            return
        if j < 0 or j >= len(grid[0]):
            return
        if grid[i][j] == "0":
            return
        grid[i][j] = '0'
        self.sink(grid, i-1, j)
        self.sink(grid, i+1, j)
        self.sink(grid, i, j-1)
        self.sink(grid, i, j+1)

from collections import deque
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0
        row = len(grid)
        col = len(grid[0])
        count = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == "1":               
                    self.bfs(grid, i, j)
                    count += 1
        return count
    
    def bfs(self, grid, i, j):
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        queue = deque([(i,j)])
        grid[i][j] = "0"
        row = len(grid)
        col = len(grid[0])
        while queue:
            x, y = queue.popleft()
            for d in directions:
                nextX = x + d[0]
                nextY = y + d[1]
                if 0 <= nextX < row and 0 <= nextY < col and grid[nextX][nextY] == "1":
                    queue.append((nextX, nextY))
                    grid[nextX][nextY] = "0"
