class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        carry = 0
        a = a[::-1]
        b = b[::-1]
        lengthA = len(a)
        lengthB = len(b)
        res = ""
        for i in range(max(lengthA, lengthB)):
            if i >= lengthA:
                addA = 0
            else:
                addA = int(a[i])
            if i >= lengthB:
                addB = 0
            else:
                addB = int(b[i])
            tmp = addA + addB + carry
            carry = int(tmp / 2)
            tmp = tmp % 2
            res += str(tmp)
        if carry == 1 and i == max(lengthA, lengthB)-1:
            res += "1"
            

        return res[::-1]
            
            