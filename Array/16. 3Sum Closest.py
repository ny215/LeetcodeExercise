class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return 0
        n = len(nums)

        mini = nums[0] + nums[1] + nums[2]
        nums.sort()
        for i in range(n-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l = i + 1
            r = n - 1
            while l < r:
                tmp = nums[i] + nums[l] + nums[r]
                if tmp == target:
                    return tmp
                
                if abs(tmp - target) < abs(mini - target):
                    mini = tmp                    
                elif tmp > target:
                    r -= 1
                elif tmp < target:
                    l += 1
        return mini
                