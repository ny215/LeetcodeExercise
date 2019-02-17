# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


#DFS recursion
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False        
        if p and q:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

#BFS use queue

import collections
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        
        queue = collections.deque([(p, q)])
        while queue:
            nodeP, nodeQ = queue.popleft()
            if not nodeP and not nodeQ:
                continue
            elif not nodeP or not nodeQ:
                return False
            if nodeP and nodeQ:
                if nodeP.val != nodeQ.val:
                    return False
                queue.append((nodeP.left, nodeQ.left))
                queue.append((nodeP.right, nodeQ.right))
    
        return True