class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        
        dict1 = {}
        dict2 = {}
        list1 = list(pattern)
        list2 = list(str.split(" "))
        for i, p in enumerate(list1):
            if p not in dict1:
                dict1[p] = [i]
            else:
                dict1[p].append(i)
        for i, s in enumerate(list2):
            if s not in dict2:
                dict2[s] = [i]
            else:
                dict2[s].append(i)
        return sorted(dict1.values()) == sorted(dict2.values())