class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        banset = set(banned)
        para = re.findall("\w+",paragraph.lower())
        count = collections.Counter(para).most_common()
        for word in count:
            if word[0] not in banset:
                return word[0]
                break
            
                