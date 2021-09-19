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
def leaf(root,second_root):
    if root is None:
        return None
    if root.left is None and root.right is None:
        second_root.append(root.val)
    leaf(root.left,second_root)
    leaf(root.right,second_root)
    return second_root