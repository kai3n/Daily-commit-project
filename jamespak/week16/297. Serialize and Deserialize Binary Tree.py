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
        def s_helper(node):
            if not node:
                return ["#"]
            return [str(node.val)] + s_helper(node.left) + s_helper(node.right)
        return " ".join(s_helper(root))

        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def d_helper(data):
            val = data.pop(0)
            if val == "#":
                return None
            node = TreeNode(int(val))
            node.left = d_helper(data)
            node.right = d_helper(data)
            return node
        return d_helper(data.split(" "))
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
