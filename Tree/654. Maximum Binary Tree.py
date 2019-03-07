# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if len(nums) == 0:
            return None
        maxNum = nums[0]
        maxInd = 0
        for i in range(len(nums)):
            if nums[i] > maxNum:
                maxNum = nums[i]
                maxInd = i
        root = TreeNode(maxNum)
        root.left = self.constructMaximumBinaryTree(nums[: maxInd])
        root.right = self.constructMaximumBinaryTree(nums[maxInd+1:])
        return root
            
# time: O(n2)
# space: O(n)