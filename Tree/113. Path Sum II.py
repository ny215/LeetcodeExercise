# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


#DFS stack
class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        res = []
        if not root:
            return res
        stack = [(root, sum - root.val, [root.val])]
        while stack:
            node, val, path = stack.pop()            
            if not node.left and not node.right:
                if val == 0:       
                    res.append(path)
            if node.left:
                stack.append((node.left, val-node.left.val, path + [node.left.val]))  
            if node.right:
                stack.append((node.right, val-node.right.val, path + [node.right.val]))   
        return res
    
#DFS recursion
class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        res = []
        path = []
        if not root:
            return res
        self.dfs(root, sum, path, res)
        return res
    def dfs(self, root, sum, path, res):
        if not root.left and not root.right:
            if sum == root.val:
                path.append(root.val)
                res.append(path)
        if root.left:
            self.dfs(root.left, sum - root.val, path+[root.val], res)
        if root.right:
            self.dfs(root.right, sum - root.val, path+[root.val], res)