class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def minDepth(self, root):
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        if not root.right and root .left:
            return 1+ self.minDepth(root.left)
        if not root.left and root.right:
            return 1+ self.minDepth(root.right)
        
        return 1+ min(self.minDepth(root.left),self.minDepth(root.right))