class Solution(object):
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        if not graph:
            return False
        
        
        
        queue = collections.deque([])
        
        label = [0 for x in range(len(graph))]
        for i in range(len(graph)):
            if (len(graph[i])!=0 and label[i] == 0):
                queue.append(i)
                label[i] = 1
                while(queue):
                    curr = queue.popleft()
                    currlabel = label[curr]
                    for nextitem in graph[curr]:
                        if (label[nextitem] == currlabel):
                            return False
                        if (label[nextitem] == 0):
                            label[nextitem] = currlabel*-1
                            queue.append(nextitem)
        return True