class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isSameTree(p, q):
        if not p and not q :
            return True
        if not p or not q or p.val!=q.val:
            return False
        return isSameTree(p.left,q.left)and isSameTree(p.right,q.right)


tree1=TreeNode(1) 
tree1.right=TreeNode(2)   
tree1.right.left=TreeNode(3)

tree2=TreeNode(1) 
tree2.right=TreeNode(2)   
tree2.right.left=TreeNode(4)


print(isSameTree(tree1,tree2))           