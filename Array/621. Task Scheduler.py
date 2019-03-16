class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        counter = [0] * 26
        for task in tasks:
            counter[ord(task) - ord('A')] += 1
        maxcount = max(counter)
        t = counter.count(maxcount)
        return max(len(tasks), (maxcount -1) *(n+1) + t)