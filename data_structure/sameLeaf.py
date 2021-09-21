class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def leafSimilar(self, root1, root2):
        a=leaf(root1,[])
        b=leaf(root2,[])
        if a==b:
            return True
def leaf(root,temp):
    if root is None:
        return None
    if root.left is None and root.right is None:
        temp.append(root.val)
    leaf(root.left,temp)
    leaf(root.right,temp)
    return temp