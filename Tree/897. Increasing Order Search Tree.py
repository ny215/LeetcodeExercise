# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorder(self,root):
        res = []
        self.helper(root, res)
        return res
    
    def helper(self, root, res):        
        if root:
            self.helper(root.left, res)
            res.append(root.val)
            self.helper(root.right,res)
    
    
    
    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        
        ans = node = TreeNode(None)
        for n in self.inorder(root):
            node.right = TreeNode(n)
            node = node.right
        return ans.right
            