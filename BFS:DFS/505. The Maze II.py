from collections import deque
class Solution(object):
    def shortestDistance(self, maze, start, destination):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: int
        """
        row = len(maze)
        col = len(maze[0])
        direction = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        queue = deque([start])
        distance = [[float("inf")]*col for _ in xrange(row)]
        distance[start[0]][start[1]] = 0
        length = 0
        
        while queue:
            curr = queue.popleft()
            for d in direction:
                x = curr[0]+ d[0]
                y = curr[1]+ d[1]
                count = 0
                while 0 <= x < row and 0 <= y < col and maze[x][y] == 0:
                    x += d[0]
                    y += d[1]
                    count += 1

                if distance[curr[0]][curr[1]] + count < distance[x - d[0]][y - d[1]]:
                    distance[x - d[0]][y - d[1]] =  distance[curr[0]][curr[1]] + count
                    queue.append([x - d[0], y - d[1]])
        if distance[destination[0]][destination[1]] == float("inf"):
            return -1
        else:
            return distance[destination[0]][destination[1]]
                    