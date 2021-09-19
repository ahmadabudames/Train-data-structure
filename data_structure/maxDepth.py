class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def max_depth(self,root):
        if not root :
            return 0
        return 1+ max(self.max_depth(root.left),self.max_depth(root.right))


        
                   