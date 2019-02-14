class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        carry = 1
        length = len(digits)
        
        for i in range(length-1,-1,-1):     #without reverse the list
            digits[i] = digits[i] + carry
            if digits[i] >= 10:
                digits[i] -= 10
                carry = 1
            else:
                carry = 0
                break

        if carry == 1 and i == 0:
            digits.insert(0,1)
        return digits

    