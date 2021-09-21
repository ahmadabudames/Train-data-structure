
class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right


def mergeTrees( t1, t2):
        if t1==None and t2==None:
            return None
        elif t1==None:
            return t2
        elif t2==None:
            return t1
        else:
           current = TreeNode(t1.val+t2.val)
           current.left=mergeTrees(t1.left,t2.left)
           current.right=mergeTrees(t1.right,t2.right)
           return current
           
           


tree1 = TreeNode(3)

tree1.left = TreeNode(9)
tree1.right = TreeNode(20)

tree1.left.left = TreeNode(5)

tree1.right.left = TreeNode(15)
tree1.right.right = TreeNode(7)

tree2 = TreeNode(5)

tree2.left = TreeNode(8)
tree2.right = TreeNode(19)

tree2.left.left = TreeNode(4)

tree2.right.left = TreeNode(5)
tree2.right.right = TreeNode(7)


    
print(mergeTrees(tree1,tree2))          


