
class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

def increasingBST(self, root):
        arr = []
        
        def inorder(root):
            
            if not root:
                return []
            inorder(root.left)
            arr.append(root.val)
            inorder(root.right)
        inorder(root)
        
        new_root = TreeNode(arr[0])
        temp = new_root
        for i in range(1,len(arr)):
            temp.right = TreeNode(arr[i])
            temp = temp.right
        return new_root
