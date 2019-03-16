class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        if not nums1 or not nums2:
             return []
        freq = {}
        for n in nums1:
            if n not in freq:
                freq[n] = 1
            else:
                freq[n] += 1
        res = []
        
        for n in nums2:
            if n in freq:
                if freq[n] > 0:
                    res.append(n)
                    freq[n] -= 1
        tmp = list(set(res))
        return tmp

#time: O(n)
#space: O(n)


#use set
class Solution:
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """  
        set1 = set(nums1)
        set2 = set(nums2)
        return list(set2 & set1)
#Time: O(n+m) in the average case and O(n×m)        
#Space: O(n+m) 