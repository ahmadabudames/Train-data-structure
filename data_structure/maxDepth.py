class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def max_depth(root):
        if not root :
            return 0
        rl=  max_depth(root.left)  
        rr= max_depth(root.right)
        return 1+ max(rl,rr)



tree1=TreeNode(1) 
tree1.right=TreeNode(2)   
tree1.left=TreeNode(3)




print(max_depth(tree1))         


        
                   