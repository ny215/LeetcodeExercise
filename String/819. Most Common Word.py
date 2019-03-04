class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        banset = set(banned)
        if not paragraph:
            return ""
        #remove punctuation
        para = re.sub(r'[^a-zA-Z]', ' ', paragraph).lower().split()
        print para
        #record the most commmon word
        count = 0
        freq = {}
        for p in para:
            if p in banset:
                continue
            if p not in freq:
                freq[p] = 1
            else:
                freq[p] += 1
            count = max(freq[p], count)
        for key in freq:
            if freq[key] == count:
                return key
#time: O(n)
#space: O(n)
        
