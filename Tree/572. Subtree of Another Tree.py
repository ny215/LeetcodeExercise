# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        return self.check(s, t)
    
    def checkvalue(self, s, t):
        if not s and not t:
            return True
        elif not s or not t:
            return False
        return (s.val == t.val) and self.checkvalue(s.left, t.left) and self.checkvalue(s.right, t.right)

        
    def check(self, s, t):
        if not s and not t:
            return True
        if not s or not t:
            return False
        if s.val == t.val and self.checkvalue(s.left, t.left) and self.checkvalue(s.right, t.right):
            return True
        return self.check(s.left, t) or self.check(s.right, t)
        