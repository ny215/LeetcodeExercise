import sys
from collections import deque
class Solution(object):
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: None Do not return anything, modify rooms in-place instead.
        """
        if rooms:
            row = len(rooms)
            col = len(rooms[0])
            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            queue = deque()
            for i in range(row):
                for j in range(col):
                    if rooms[i][j] == 0:
                        queue.append([i, j])
            while queue:
                curr = queue.popleft()
                for d in directions:
                    x = curr[0] + d[0]
                    y = curr[1] + d[1]
                    if 0<=x < row and 0 <= y <col and rooms[x][y] > rooms[x-d[0]][y-d[1]]:
                        rooms[x][y] = rooms[x-d[0]][y-d[1]] + 1
                        queue.append([x,y])