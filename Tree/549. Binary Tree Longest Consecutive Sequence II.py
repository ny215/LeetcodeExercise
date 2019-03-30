# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        self.res = 1
        self.dfs(root)
        return self.res
    
    def dfs(self, root):
        if not root: 
            return [0, 0]
        inc, dec = 1, 1
        left = self.dfs(root.left)
        right = self.dfs(root.right)
        
        if root.left:
            if root.left.val - 1 == root.val:
                inc = max(inc, left[0]+1)
            if root.left.val + 1 == root.val:
                dec = max(dec, left[1]+1)
        if root.right:
            if root.right.val - 1 == root.val:
                inc = max(inc, right[0] + 1)
            if root.right.val + 1 == root.val:
                dec = max(dec, right[1] + 1)
        self.res = max(self.res, inc+dec-1)
        return [inc, dec]
        