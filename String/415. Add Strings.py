class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        #ord('0')
        carry = 0
        n1 = num1[::-1]
        n2 = num2[::-1]
        res = ""
        l = max(len(n1), len(n2))
        for i in range(l):
            if i < len(n1):
                v1 = ord(n1[i]) - ord('0')
            else:
                v1 = 0
            if i < len(n2):
                v2 = ord(n2[i]) - ord('0')
            else:
                v2 = 0
            tmp = (v1 + v2 + carry) % 10
            carry = (v1 + v2 + carry) / 10
            res += str(tmp)
        if carry:
            res += str(carry)
        return res[::-1]