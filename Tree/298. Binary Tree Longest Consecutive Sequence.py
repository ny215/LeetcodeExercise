# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution(object):
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        res = 1
        depth = 1
        queue = deque([(root,depth)])
        while queue:
            node, d = queue.popleft()
            if node.left:
                if node.val + 1 == node.left.val:
                    res = max(res, d+1)
                    queue.append((node.left, d+1))
                else:
                    queue.append((node.left, 1))
            if node.right:
                if node.val + 1 == node.right.val:
                    res = max(res,d+1)
                    queue.append((node.right, d+1))
                else:
                    queue.append((node.right, 1))
        return res
