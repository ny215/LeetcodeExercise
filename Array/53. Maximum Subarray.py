#dp
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

#basic dp
class Solution:
    def maxSubArray(self, nums):
    if not nums:
        return 0
    dp = [0] * len(nums)
    dp[0] = nums[0]
    maxsum = dp[0]
    for i in range(1, len(nums)):
        dp[i] = max((dp[i-1]+ nums[i]), nums[i])
        maxsum = max(maxsum, dp[i])
    return maxsum
