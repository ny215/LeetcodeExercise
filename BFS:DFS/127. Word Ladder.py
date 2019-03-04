from collections import deque
from collections import defaultdict

class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        #edge case
        if not endWord in wordList or not beginWord or not endWord or not wordList:
            return 0
        visited ={}
        #default dict with values are list. store candidate words
        cand = defaultdict(list)
        n = len(beginWord)
        for word in wordList:
            for i in range(n):
                cand[word[:i]+"*"+ word[i+1:]].append(word)
        #bfs searching
        queue = deque([(beginWord, 1)])
        visited[beginWord] = True
        while queue:
            curr, count = queue.popleft()
            for i in range(n):
                nextWord = curr[:i] + "*" + curr[i+1:]
                for word in cand[nextWord]:
                    if word == endWord:
                        count += 1
                        return count
                    if word not in visited:
                        visited[word] = True
                        queue.append((word, count+1))
           # cand[nextWord] = []
        return 0
        