#if the remainder is same, then the difference between i,j can be divided by k
class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        dic = {}
        sum = 0
        dic[0] = -1 #same like 560. need someone to represent 0
        for i in range(len(nums)):
            sum += nums[i]
            if k != 0:
                sum = sum % k
            if sum in dic:
                if i - dic[sum] > 1: #meet the requirement of length
                    return True
            else:
                dic[sum] = i
        return False
#O(n)
#O(min(n,k))



class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        listsum = [0 * x for x in range(len(nums))]
        listsum[0] = 0
        for i in range(1, len(nums)):
            listsum[i] = listsum[i-1] + nums[i]
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                tmp = listsum[j] - listsum[i] + nums[i]
                if tmp == k or (k != 0 and tmp%k == 0):
                    return True
        return False

#O(n2), memo the sum to reduce time
#O(n)
