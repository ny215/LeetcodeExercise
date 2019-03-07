class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True

        pair = {
            "(":")",
            "{":"}",
            "[":"]"
        }
        tmp = []
        for n in s:
            if n in pair:
                tmp.append(pair[n])
            else:
                if not tmp:
                    return False
                if tmp.pop() != n:
                    return False
        return not tmp
# time: O(n)
# space: O(n)