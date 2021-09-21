class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



def rangeSumBST( root, low, hight):

        if not root :
            return 0
        if low > root.val:
            return rangeSumBST(root.right,low ,hight)
        if hight <root.val :
            return rangeSumBST(root.left,low, hight)

        else:
            return rangeSumBST(root.left,low,hight)+root.val + rangeSumBST(root.right, low ,hight)     


tree1=TreeNode(5) 
tree1.right=TreeNode(2)   
tree1.left=TreeNode(3)
tree1.left.left=TreeNode(6)





print(rangeSumBST(tree1,3,6))         


    
