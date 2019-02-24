class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        checks = {}
        checkt ={}
        for i, letter in enumerate(s):
            if letter not in checks:
                checks[letter] = [i]
            else:
                checks[letter].append(i)
        for i, letter in enumerate(t):
            if letter not in checkt:
                checkt[letter] = [i]
            else:
                checkt[letter].append(i)
        return sorted(checkt.values()) == sorted(checks.values())
