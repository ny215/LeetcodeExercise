# The knows API is already defined for you.
# @param a, person a
# @param b, person b
# @return a boolean, whether a knows b
# def knows(a, b):

class Solution(object):
    def findCelebrity(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 0
        right = n-1
        while left < right:
            if knows(left, right):
                left += 1 #left one is not the candidate because celebrity doesn't know others
            else:
                right -= 1 #right one is not the candidate because everyone knows celebrity
        for i in range(n):
            if (i != left) and knows(left, i) or not knows(i, left):
                return -1
        return left