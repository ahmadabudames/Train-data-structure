


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def preorderTraversal( root):
    if root is None:
        return []
    global ans  
    ans = []

    def preorder (root):
        global ans

        ans.append(root.val)

        if root.left :
            preorder(root.left)
        if root.right:
            preorder(root.right)
        

    preorder(root)

    return ans          
        

tree=TreeNode(1) 
tree.left=TreeNode(5)   
tree.right=TreeNode(2)
print(preorderTraversal(tree))    