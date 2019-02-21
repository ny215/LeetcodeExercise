class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        counts = [0] * 10
        bull = 0
        cow = 0
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bull += 1
            else:
                ind1 = int(secret[i])
                counts[ind1] += 1
                if counts[ind1] <= 0:
                    cow += 1
                ind2 = int(guess[i])
                counts[ind2] -= 1
                if counts[ind2] >= 0:
                    cow += 1
                
                    
        res = str(bull) + "A" + str(cow) + "B"
        return res


#
class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        counts1 = [0] * 10
        counts2 = [0] * 10
        bull = 0
        cow = 0
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bull += 1
            else:
                ind1 = int(secret[i])
                counts1[ind1] += 1
                
                ind2 = int(guess[i])
                counts2[ind2] += 1
        for i in range(len(counts1)):
            cow += min(counts1[i], counts2[i])
                
                    
        res = str(bull) + "A" + str(cow) + "B"
        return res

        
        