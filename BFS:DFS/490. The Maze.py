class Solution(object):
    def hasPath(self, maze, start, destination):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: bool
        """
        row = len(maze)
        col = len(maze[0])
        visited = [[0]*col for _ in xrange(row)]
        queue = collections.deque([start])
        directions =[[0, 1], [0, -1], [1, 0], [-1, 0]]
        while queue:
            curr = queue.popleft()
            if(curr[0] == destination[0] and curr[1] == destination[1]):
                return True
            
            # Roll the ball until it hits a wall
            for d in directions:
                x = curr[0] + d[0]
                y = curr[1] + d[1]
                while 0 <= x < row and 0 <=y < col and maze[x][y] == 0:
                    x += d[0]
                    y += d[1]
                # Check if the new starting position has been visited   
                #roll back one step as the ball is "in the wall"
                if visited[x-d[0]][y-d[1]] == 0:
                    queue.append([x-d[0],y-d[1]])
                    visited[x-d[0]][y-d[1]] = 1
        return False