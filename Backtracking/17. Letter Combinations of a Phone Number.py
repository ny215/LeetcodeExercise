class Solution(object):
    
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        check = {
            '2': ['a','b','c'],
            '3': ['d','e','f'],
            '4': ['g','h','i'],
            '5': ['j','k','l'],
            '6': ['m','n','o'],
            '7': ['p','q','r','s'],
            '8': ['t','u','v'],
            '9': ['w','x','y','z']
        }    
        res = []
        if not digits:
            return []
        self.backtrack("", digits, res, check)
        return res
   
    def backtrack(self, comb, nextdigit, res, check):
        if len(nextdigit) == 0:
            res.append(comb)
        else:
            for letter in check[nextdigit[0]]:
                self.backtrack(comb+letter, nextdigit[1:], res, check)
#Time complexity : \mathcal{O}(3^N \times 4^M)where N is the number of digits in the input that maps to 3 letters (e.g. 2, 3, 4, 5, 6, 8) and M is the number of digits in the input that maps to 4 letters (e.g. 7, 9), and N+M is the total number digits in the input.

#Space complexity : \mathcal{O}(3^N \times 4^M)