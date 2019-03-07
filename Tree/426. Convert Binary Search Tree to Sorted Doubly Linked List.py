"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right
"""
class Solution(object):
    def treeToDoublyList(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return None
        head, tail = self.helper(root)
        return head
    
    def helper(self, root):
        head, tail = root, root
        if root.left:
            leftHead, leftTail = self.helper(root.left)
            leftTail.right = root
            root.left = leftTail
            head = leftHead
        if root.right:
            rightHead, rightTail = self.helper(root.right)
            rightHead.left = root
            root.right = rightHead
            tail = rightTail
        head.left = tail
        tail.right = head
        return head, tail
# Time: O(v), v是二叉树的节点数目
# Space: O(v)