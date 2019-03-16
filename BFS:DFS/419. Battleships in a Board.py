#O(1) space
#check the ship from the top-left corner of the ship.
class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """

        if not board or not board[0]:
            return 0
        count = 0
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] != "X":
                    continue
                if i > 0 and  board[i-1][j] == "X":
                    continue
                if j > 0 and board[i][j-1] == "X":
                    continue
                count += 1
        return count

#bfs
from collections import deque
class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """

        if not board or not board[0]:
            return 0
        res = 0
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "X":
                    self.bfs(board, i, j)
                    res += 1
        return res
    
    
    def bfs(self, board, i, j):
        queue = deque([(i,j)])
        board[i][j] = "#"            

        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        while queue:
            x, y = queue.popleft()
            for d in directions:
                currX = x + d[0]
                currY = y + d[1]
                if 0 <= currX < len(board) and 0 <= currY < len(board[0]) and board[currX][currY] == "X":
                    queue.append((currX, currY))
                    board[currX][currY] = "#"            
            