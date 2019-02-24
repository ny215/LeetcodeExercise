class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = "aeiouAEIOU"
        start = 0 
        end = len(s)-1
        s = list(s) #convert string into list
        while start < end:
            if s[start] not in vowels:
                start += 1
            if s[end] not in vowels:
                end -= 1
            if s[start] in vowels and s[end] in vowels:
                s[start], s[end] = s[end], s[start]
                start += 1
                end -= 1

        return "".join(s)
                