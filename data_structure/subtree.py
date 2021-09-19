class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def isSubtree(self, root, subRoot):
        if root is None:
            return False
        if self.sameTree(root,subRoot):
            return True
        else:
            return self.isSubtree(root.right,subRoot)or self.isSubtree(root.left,subRoot)
        
    def sameTree(self, root , subRoot):
        if root is None or subRoot is None :
            return root is None and subRoot is None
        if root.val==subRoot.val:
            return self.sameTree(root.right,subRoot.right) and self.sameTree(root.left,subRoot.left)