#heap1
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


#heap2
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
        for word in dic:
            res.append([word, dic[word]])
        heap = heapq.nsmallest(k, res, key = lambda x: (-x[1],x[0]))
        print heap
        return  [i[0] for i in heap]

#sort
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
        for word in dic:
            res.append([word, dic[word]])
        res.sort(key = lambda x:(-x[1], x[0]))
        return  [i[0] for i in res][:k]
            