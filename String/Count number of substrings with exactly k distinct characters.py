"""
Given a string of lowercase alphabets, count all possible substrings (not necessarily distinct) that has exactly k distinct characters.
Examples:

Input: abc, k = 2
Output: 2
Possible substrings are {"ab", "bc"}

Input: aba, k = 2
Output: 3
Possible substrings are {"ab", "ba", "aba"}

Input: aa, k = 1
Output: 3
Possible substrings are {"a", "a", "aa"}

"""
def NumberOfSubstringKDistinct(s, k):
    """
    :type s: str
    :rtype: int
    """
    n = len(s)
    #initialize result
    res = 0
    count = [0]*27
    string = []
    for i in range(n):
        disCount = 0
        count = [0]*27
        tmp = "" #if the substring need to be returned.
        for j in range(i,n):
            #it new character, increment disCount
            if(count[ord(s[j]) -97]) == 0:
               disCount += 1
            count[ord(s[j]) -97] += 1
            tmp += (s[j])
            if(disCount == k):
                res += 1
                string.append(tmp)
            if(disCount > k):
                break
    return string
                
