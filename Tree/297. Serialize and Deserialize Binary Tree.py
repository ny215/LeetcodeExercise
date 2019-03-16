# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        def serial(root, res):
            if not root:
                res +='None,'
            if root:
                res += str(root.val) + ","
                res = serial(root.left, res)
                res = serial(root.right, res)
            print res
            return res
        
        return serial(root, "")

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def deserial(data):
            if not data:
                return None
            if data[0] == "None":
                data.pop(0)
                return None
            root = TreeNode(data[0])
            data.pop(0)
            root.left = deserial(data)
            root.right = deserial(data)
            return root
        l = data.split(",")
        root = deserial(l)
        return root
        
        
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))