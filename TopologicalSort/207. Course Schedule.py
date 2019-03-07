class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        graph = [[] for _ in range(numCourses)]
        for course, prerequisite in prerequisites:
            graph[course].append(prerequisite)
        #state: 0: unknown, 1: visiting, 2:visited
        visit = [0 for _ in range(numCourses)]
        for i in range(numCourses):
            if self.dfs(graph, i, visit):
                return False
        return True
    
    def dfs(self, graph, curr, visit):
        #cycle
        if visit[curr] == 1:
            return True     
        if visit[curr] == 2:
            return False
        visit[curr] = 1
        for n in graph[curr]:
            if self.dfs(graph, n, visit):
                 return True
        visit[curr] = 2
        return False
#Topological sort O(N + E)
#Space: O(n)        