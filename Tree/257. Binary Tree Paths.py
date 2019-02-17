# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


#DFS recursion
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        res = []
        if not root:
            return res
        tmp = ""
        self.dfs(root, tmp, res)
        return res
    
    def dfs(self, root, tmp, res):
        if not root.left and not root.right:
            tmp = tmp + str(root.val)
            res.append(tmp)
        if root.left:
            self.dfs(root.left, tmp+ str(root.val)+ "->", res)
        if root.right:
            self.dfs(root.right, tmp+ str(root.val)+ "->", res)
