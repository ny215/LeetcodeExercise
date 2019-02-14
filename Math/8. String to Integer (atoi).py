class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        if len(str) == 0:
            return 0
        string = list(str.strip())
        if len(string) == 0:
            return 0
        
        sign = 1
        if string[0] == "-":
            sign = -1
        elif string[0] == "+":
            sign = 1
        if string[0] in ["-", "+"]:
            string = string[1:]
            
        res = 0
        i = 0
        while  i < len(string) and ord(string[i]) >= 48 and ord(string[i]) <= 57: #not a number； ord('0') == 48
            res = res*10 + ord(string[i]) - 48
            i += 1
        if sign == -1:
            return max(res*sign,pow(-2,31))
        if sign == 1:
            return min(res*sign,pow(2,31)-1)