# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#DFS recursion
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        return root
#time: O(n)
#space: O(h)

#BFS queue
from collections import deque
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if node:
                node.left, node.right = node.right, node.left
                queue.append(node.left)
                queue.append(node.right)
        return root

#time: O(n)
#space: O(n)
