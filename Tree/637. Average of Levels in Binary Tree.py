# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        if not root:
            return []
        res = []
        queue = [root]
        while queue:
            tmp = 0
            for node in queue:
                tmp += node.val   
            res.append(tmp*1.0/len(queue)) 
            curr =[]      
            for node in queue:
                if node.left:
                    curr.append(node.left)
                if node.right:
                    curr.append(node.right)
            queue = curr
            
        return res
# time: O(n)
# space: O(m) max number of leaf in one level