# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution(object):
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        cols = collections.defaultdict(list)
        queue = deque([(root, 0)])
        while queue:
            node, level = queue.popleft()
            if node:
                cols[level].append(node.val)
                queue.append((node.left, level - 1))
                queue.append((node.right, level + 1))
        key = sorted(cols.keys())
        res = []
        for i in key:
            res.append(cols[i])
        return res
