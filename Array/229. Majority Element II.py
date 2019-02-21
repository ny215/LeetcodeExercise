#Boyer-Moore Algorithm
#https://gregable.com/2013/10/majority-vote-algorithm-find-majority.html

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []
        count1, count2, candidate1, candidate2 = 0, 0, 0, 1
        for n in nums:
            if n == candidate1:
                count1 += 1
            elif n == candidate2:
                count2 += 1
            elif count1 == 0:
                candidate1, count1 = n, 1
            elif count2 == 0:
                candidate2, count2 = n, 1
            else:
                count1, count2 = count1 - 1, count2 - 1
                
        res = []
        if nums.count(candidate1) > len(nums) // 3:
            res.append(candidate1)
        if nums.count(candidate2) > len(nums)// 3:
            res.append(candidate2)
        
        return res
    