
class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

def increasingBST(root):
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
        return new_root.val


if __name__ == "__main__":

    tree1 = TreeNode(3)

    tree1.left = TreeNode(9)
    tree1.right = TreeNode(20)

    tree1.left.left = TreeNode(5)

    tree1.right.left = TreeNode(15)
    tree1.right.right = TreeNode(7)

    print(f"sumOfLeaves: {increasingBST(tree1)}")        
