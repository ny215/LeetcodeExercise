class Solution(object):
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        res = []
        digit = []
        letter = []
        for log in logs:
            if (log.split(" ")[1][0]).isnumeric():
                digit.append(log)
            else:
                letter.append(log)
        
        def sortKey(l):
            return l.split(" ")[1:]
        
        letter.sort(key = sortKey)
        return letter + digit