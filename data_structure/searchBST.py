class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def searchBST(root, val):
        if root is None:
            return None
        while root:
            if root.val==val:
                return root
            elif root.val < val:
                 root=root.right
            else:
                 root =root.left
        return root        

tree1=TreeNode(1) 
tree1.right=TreeNode(2)   
tree1.right.left=TreeNode(3)




print(searchBST(tree1,2))               