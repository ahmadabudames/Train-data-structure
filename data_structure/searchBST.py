   def searchBST(self, root, val):
        if root is None:
            return None
        while root:
            if root.val==val:
                return root
            elif root.val < val:
                 root=root.right
            else:
                 root =root.left