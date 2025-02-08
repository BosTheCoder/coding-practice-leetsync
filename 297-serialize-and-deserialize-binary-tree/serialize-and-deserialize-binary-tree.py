# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    NULL_VAL = 1001
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        ret = ""
        def preorder(node):
            nonlocal ret
            ret += f"{node.val}," if node else f"{self.NULL_VAL},"
            if not node:
                return
            preorder(node.left)
            preorder(node.right)
        preorder(root)
        ret = ret[:-1]
        # print(ret)
        return ret

        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        data = data.split(",")
        def preorder(i):
            
            if i>=len(data):
                return None, 0
            val = int(data[i])
            # print(f"running preorder for {val}, i={i}")
            
            if val == self.NULL_VAL:
                return None, 1
            curr = TreeNode(int(val))
            left,leftlen = preorder(i + 1)
            # print(f"left preorder for {val} returned {left},{leftlen}")
            curr.left = left
            right,rightlen = preorder(i + 1 + leftlen)
            # print(f"right preorder for {val} returned {right},{rightlen}")
            curr.right = right
            # print(f"curr for {val} = {curr}")
            return curr, 1 + leftlen + rightlen
        return preorder(0)[0]

        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))