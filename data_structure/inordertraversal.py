class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# class Solution(object):
def inorderTraversal(root,target):
    if root is None:
         return []
    global arr
    arr = []     
    
    def inorder(root):

        global arr
        if root.left :
            inorder(root.left)
        arr.append(root.val)

        if root.right:
            inorder(root.right)

    inorder(root)
    final=[]
    for i in range(len(arr)+1):
        if arr[i]+arr[i+1]==target:
            final.append(arr[i])
            final.append(arr[i+1])
            
    return arr[final]

        
    

        

  
     
     
tree=TreeNode(1) 
tree.right=TreeNode(2)   
tree.right.left=TreeNode(5)
print(inorderTraversal(tree,3))     