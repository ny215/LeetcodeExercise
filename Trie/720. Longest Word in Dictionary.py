class TrieNode:
    def __init__(self):
        self.isWord = False
        self.word = ""
        self.children = {}
        
class Solution(object):
    def __init__(self):        
        self.root = TrieNode()
    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        #insert
        for word in words:
            curr = self.root
            for letter in word:
                if letter not in curr.children:
                    curr.children[letter] = TrieNode()
                curr = curr.children[letter]
            curr.isWord = True
            curr.word = word
            
        #search
        res = ""
        curr = self.root
        stack = list(curr.children.values())
        while stack:
            node = stack.pop(-1)
            if node.isWord:
                print node.word
                if len(res) < len(node.word) or (len(res) == len(node.word) and res > node.word):
                    res = node.word
                stack.extend((list(node.children.values())))
        return res

#time: O(sum(word[i]))
#space: O(26*n*w)