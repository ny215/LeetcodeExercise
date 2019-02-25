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
class Solution(object):
def NumberOfSubstringKDistinct(s, k):
    """
    :type s: str
    :rtype: int
    """
    dic = {}
    res = []
    start = 0
    end = 0
    n = len(s)
    count = 0
    for end in range(n):
        dic[s[end]] = end
        end += 1
        #if the length == k, then add it to res
        if len(dic) == k:  
            res.append(s[start:end])
        #if the length > k, then remove item in the substring from the front
        if len(dic) > k:
            delIndex = min(dic.values())
            del dic[s[delIndex]]
            start = delIndex + 1
    # add the last substring that meets the requirment
    if len(dic) == k:
        res.append(s[start:end])
    #remove duplicate
    return list(set(res))
