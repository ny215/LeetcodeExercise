# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        self.dfs(root, res, 0)
        return res
    def dfs(self, root, res,height):
        if root != None:
            if len(res) < height +1:
                res.append([])
            res[height].append(root.val)
            height += 1
            self.dfs(root.left, res, height)
            self.dfs(root.right, res, height)
     


#BFS: traverse level by level (just like the way the question asked)
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        queue = [(root, 0)]
        while queue:
            node, level = queue.pop(0)
            if node:
                if len(res) < level+1:
                    res.append([])
                res[level].append(node.val)
                queue.append((node.left, level+1))
                queue.append((node.right,level+1))
        return res