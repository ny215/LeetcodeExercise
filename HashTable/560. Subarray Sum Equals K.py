class Solution:
    def subarraySum(self, nums, target):
        dic = {}
        dic[target] = [-1]
        listsum = [0 for x in xrange(len(nums))]
        listsum[0] = nums[0]
        for i in range(1, len(nums)):
            listsum[i] = listsum[i-1] + nums[i]
        count = 0
        for i, s in enumerate(listsum):
            if s in dic:
                count += len(dic[s])   
            if s + target not in dic:
                dic[s + target] = [i]
            else:
                dic[s + target].append(i)
            
        return count
                
            
#time: O(n)
#space: O(n)
#similar to Two Sum        