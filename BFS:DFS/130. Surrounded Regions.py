#BFS
from collections import deque
class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
    
        if not board or not board[0]:
            return
        queue = deque([])
        row = len(board)
        col = len(board[0])
        for i in xrange(row):
            for j in xrange(col):
                if (i in [0, row-1] or j in [0, col-1]) and board[i][j] == "O":
                    queue.append([i,j])
        directions = [[0, 1], [0, -1], [1, 0],[-1, 0]]
        while queue:
            r, c = queue.popleft()
            if 0<=r<len(board) and 0<=c<len(board[0]) and board[r][c] == "O":
                board[r][c] = "Z"
                queue.append((r-1, c)); queue.append((r+1, c))
                queue.append((r, c-1)); queue.append((r, c+1))
                
        for i in xrange(row):
            for j in xrange(col):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "Z":
                    board[i][j] = "O"
                
                    
        