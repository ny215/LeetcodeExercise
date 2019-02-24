class Solution(object):
    def reverseWords(self, str):
        """
        :type str: List[str]
        :rtype: void Do not return anything, modify str in-place instead.
        """
        str.reverse()
        start = 0
        for i in range(len(str)):
            if str[i] == " ":
                str[start:i] = reversed(str[start:i])
                start = i+1
        str[start: ] = reversed(str[start: ])

                
            