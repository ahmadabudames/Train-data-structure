


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def postorderTraversal(root):  
    if root is None:
        return []
    global ans 
    ans =[]

    def postorder(root):
        global ans

        

        if root.left:
            postorder(root.left)

        if root.right:
            postorder(root.right)

        ans.append(root.val)    
    postorder(root)

    return ans                


tree=TreeNode(1) 
tree.right=TreeNode(2)   
tree.left=TreeNode(5)
print(postorderTraversal(tree))   