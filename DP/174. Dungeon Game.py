class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        if not dungeon or not dungeon[0]:
            return 0
        row = len(dungeon)
        col = len(dungeon[0])
         #from bottom right to current grid, how many hp we need
        hp =[[float('inf')]* (col+1) for _ in xrange(row+1)]
        hp[row][col-1] = hp[row-1][col] = 1
        for x in xrange(row-1, -1, -1):
            for y in xrange(col-1, -1, -1):
                hp[x][y] = max(1, min(hp[x+1][y], hp[x][y+1]) - dungeon[x][y])               
        return hp[0][0]