# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#iterate
class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False
        stack = [(root, root.val)]
        while stack:
            node, val = stack.pop()
            if not node.left and not node.right:
                if val == sum:
                    return True
            #while updating the remaining sum to cumulate at each visit.
            if node.left:
                stack.append((node.left, val+node.left.val))  
            if node.right:
                stack.append((node.right, val+node.right.val))            
        return False

#recursion 

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False
        sum -= root.val
        if not root.left and not root.right:
            if sum == 0:
                return True
        return self.hasPathSum(root.left, sum) or self.hasPathSum(root.right, sum)