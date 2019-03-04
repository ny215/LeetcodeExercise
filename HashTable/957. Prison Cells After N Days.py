class Solution(object):
    def prisonAfterNDays(self, cells, N):
        """
        :type cells: List[int]
        :type N: int
        :rtype: List[int]
        """
        if N > 14:
            N =  N%14
        if N%14 == 0:
            N = 14
        for i in range(1, N+1):
            tmp = [0]*len(cells)
            for i in range(1, len(cells)-1):
                if cells[i-1] == cells[i+1]:
                    tmp[i] = 1
            cells = tmp
        return cells
                  