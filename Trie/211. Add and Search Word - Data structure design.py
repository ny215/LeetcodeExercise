class TrieNode(object):
    def __init__(self):
        self.children = {}        
        self.isWord = False
        
class WordDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()
        
    
    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: None   
        """
        node = self.root
        for letter in word:
            if letter not in node.children:
                node.children[letter] = TrieNode()
            node = node.children[letter]
        node.isWord = True
        
    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        stack = [(self.root, word)]
        while stack:
            node, w = stack.pop()
            if not w:
                if node.isWord:
                    return True
            elif w[0] == ".":
                for n in node.children.values():
                    stack.append((n, w[1:]))
            else:
                if w[0] in node.children:
                    n = node.children[w[0]]
                    stack.append((n, w[1:]))
        return False
        



# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)





#use bfs      
    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        node = self.root
        self.res = False
        self.dfs(node, word)
        return self.res
    
    def dfs(self, node, word):
        if not word:
            if node.isWord:
               self.res = True
            return
        
        if word[0] == ".":
            for n in node.children.values():
                self.dfs(n, word[1:])
        else:
            node = node.children.get(word[0])
           # if word[0] not in node.children:
            if not node:
                return
            self.dfs(node, word[1:])

        



# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)