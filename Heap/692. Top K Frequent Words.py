class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        dic = {}
        res = []
        for word in words:
            if word not in dic:
                dic[word] = 1
            else:
                dic[word] += 1
        return heapq.nsmallest(k, dic, key=lambda word:(~dic[word], word))