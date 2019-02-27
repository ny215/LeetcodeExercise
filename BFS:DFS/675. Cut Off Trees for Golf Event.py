class Solution(object):
    def cutOffTree(self, forest):
        """
        :type forest: List[List[int]]
        :rtype: int
        """
        res = 0
        r, c = len(forest), len(forest[0])
        trees = []
        for i in xrange(r):
            for j in xrange(c):
                if forest[i][j] > 1:
                    trees.append((forest[i][j], i, j))
        trees.sort()
        sr = 0
        sc = 0
        for i in range(len(trees)):
            tr = trees[i][1]
            tc = trees[i][2]
            dis = self.BFS(forest, sr, sc, tr, tc)
            if dis == -1:
                return -1
            res += dis
            forest[tr][tc] = 1
            sr = tr
            sc = tc
        return res

            

    def BFS(self, forest, sr, sc, tr, tc):    
        R = len(forest)
        C = len(forest[0])
        queue = collections.deque([(sr, sc, 0)])
        seen = {(sr, sc)}
        while queue:
            r, c, d = queue.popleft()
            if r == tr and c == tc:
                return d
            for nr, nc in ((r-1, c), (r+1, c), (r, c-1), (r, c+1)):
                if 0 <= nr < R and 0<= nc < C and forest[nr][nc] and (nr, nc) not in seen:
                    seen.add((nr, nc))
                    queue.append((nr, nc, d+1))
        return -1
                