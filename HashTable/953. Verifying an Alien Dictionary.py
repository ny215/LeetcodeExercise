class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        ind = {}
        for i, letter in enumerate(order):
            ind[letter] = i
        for i in range(len(words)-1):
            word1 = words[i]
            word2 = words[i+1]
            
            for k in xrange(min(len(word1), len(word2))):
                if word1[k] != word2[k]:
                    if ind[word1[k]] > ind[word2[k]]:
                        return False
                    break
            else:
                if len(word1) > len(word2):
                    return False
        return True
#time: O(C)
# space: O(26) = O(1)