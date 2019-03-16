class Solution(object):
    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        if not S:
            return ""
        words = S.split(" ")
        vowel = "aeiouAEIOU"
        m = "ma"
        res = []
        for i, word in enumerate(words):
            tail = "a" * (i+1)
            tmp = ""
            if word[0] in vowel:
                tmp = word + m + tail
            else:
                tmp = word[1:] + word[0] + m + tail
            res.append(tmp)
        return " ".join(res)
                
# time: O(n2)    
#space: O(n2)


