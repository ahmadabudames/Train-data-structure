class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        if root is None:
            return False
        targetSum -= root.val 
        if root.left is None and root.right is None and targetSum==0:
            return True 
        return self.hasPathSum(root.left,targetSum) or self.hasPathSum(root.right,targetSum)