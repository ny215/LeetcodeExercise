#53. Maximum Subarray
class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #initialize currMax and maxMAx	
        currMax = nums[0]
        maxMax = nums[0]
        #use maxMax to track global maximum. currMax to check the effect of previous sum
        for i in range(1,len(nums)):
            currMax = max(currMax + nums[i], nums[i])
            maxMax = max(maxMax, currMax)

        return maxMax
	
#test

s = Solution()
n1 = [1,2,3]
n2 = [-1,-2,-3]
n3 = [-2,1,-3,4,-1,2,1,-5,4]
res = s.maxSubArray(n3)
print(res)